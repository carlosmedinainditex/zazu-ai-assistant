---
applyTo: "**"
description: "Instrucciones para el análisis de incidencias con el agente IA de Zazu (zazu-jira-api-connector), herramienta especializada en análisis de bugs y problemas en JIRA con integración MCP Atlassian."
author: Carlos Medina
version: 3.0
tags: ["zazu", "jira", "api", "automatizacion", "analisis", "bugs", "incidencias", "atlassian", "mcp", "ai-agent", "iopprosu"]
tools: ["atlassian", "geppetto-api", "geppeto", "github"]
globs: ["**/zazu-jira-api-connector/**/*", "**/*zazu*", "**/reports/**/*"]
---

# 🚨 INSTRUCCIONES ESPECÍFICAS - ANÁLISIS DE BUGS ZAZU
- Nunca uses Search de JIRA con MCP

## 🎯 MISIÓN: ANÁLISIS AUTOMÁTICO Y CLUSTERING DE BUGS

### Activación Específica
**Triggers de activación:**
- "bugs de [PRODUCTO]"
- "incidencias de [PRODUCTO]"
- "bugs IOPPROSU de [PRODUCTO]"
- "incidencias IOPPROSU de [PRODUCTO]"
- "bugs no-IOPPROSU de [PRODUCTO]"
- "incidencias no-IOPPROSU de [PRODUCTO]"

---

## 🔍 FLUJO DE EJECUCIÓN OBLIGATORIO

### 1. Validación de Producto (Paso Crítico)
- **Entrada:** El `[PRODUCTO]` proporcionado por el usuario (nombre o ID, ej: `ATEAM-99312`).
- **Acción:** Validar existencia del producto vía MCP.
  - **Campos a verificar:** `"Products/Enablers - Affected"` (customfield_43463) y `"Product/Enabler - Principal"` (customfield_43462).
  - **Comando:** ``"Product/Enabler - Principal"` = "[PRODUCTO]"`
- **Resultado:**
  - **✅ Éxito:** Si se encuentra el producto, continuar al siguiente paso.
  - **❌ Fracaso:** Si no se encuentra, **detener ejecución** y notificar al usuario: `No se encontró el producto "[PRODUCTO]". Por favor, verifique el nombre o ID.`.

### 2. Construcción JQL
- **Lógica de Búsqueda:**
  - **Tipo de Incidencia:** 
    - **Bug:** `issuetype = Bug` (excluir Spikes, Tasks, etc.).
    - **Spike:** `issuetype = Spike` (excluir Bugs, Tasks, etc.).
    - **IOPPROSU:** No filtrar por tipo, eliminar la clausula.
  - **Entorno:** 
    - **General/no-IOPPROSU:** `"Entorno Incidencia" = Produccion` (customfield_10824).
    - **IOPPROSU:** No filtrar por entorno, eliminar la clausula.
  - **Periodo Inicial:** `created >= -90d`.
  - **Estado:** No incluir estado DISCARDED (status not in (Discarded).
  - **Filtrado por Proyecto:**
    - Si se especifica "IOPPROSU": Añadir `AND project = "IOPPROSU"`
    - Si no se especifica: No añadir filtro de proyecto.
- **JQL Base (General):**
  ```jql
("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]") AND issetype = "Bug"AAND "Entorno Incidencia" = "Produccion" AND status not in (Discarded) AND created >= -90d ORDER BY priority DESC, created DESC
  ```
- **JQL Base (IOPPROSU):**
  ```jql
 ("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]") AND project = "IOPPROSU" AND created >= -90d AND status not in (Discarded) ORDER BY priority DESC, created DESC
  ```
- **Búsqueda Adaptativa:**
  - Si la JQL inicial no devuelve resultados, **ampliar el periodo de forma incremental** (`-180d`, `-365d`) hasta encontrar resultados o confirmar que no existen.

### 3. Ejecución JQL y Extracción de Datos 
- **Comando:** Ejecutar la JQL construida utilizando el script principal con el modo de consulta directa:
  ```bash
  ./main.sh -q "JQL_CONSTRUIDA_ANTERIORMENTE"
  ```
- **Proceso de Datos:** 
  - El script generará automáticamente un archivo JSON en `/reports/json/` con timestamp
  - **🚨 CRÍTICO:** Este archivo será la fuente de datos ÚNICA y AUTORITATIVA para el análisis

### 4. Recuperación y Validación de Contexto
- **Ubicación:** Buscar el archivo JSON más reciente por timestamp en `/reports/json/`
- **Carga:** Cargar COMPLETAMENTE todos los datos del archivo en el contexto de análisis
- **Verificación:** Confirmar que los datos son coherentes y completos antes de continuar
  ```
  ✅ Contexto cargado: [X] issues de [PRODUCTO]
  📊 Datos extraídos: [timestamp del archivo]
  🔍 Iniciando análisis profundo...
  ```
---

## 🧠 ANÁLISIS DE CLUSTERS: DE DATOS A INTELIGENCIA

### Metodología de Clustering
1.  **Agrupación por Similitud Semántica:**
    - **Componente/Módulo Afectado:** Agrupar por el componente de software común.
    - **Patrones en Descripciones:** Identificar patrones recurrentes en los resúmenes y descripciones. Buscar palabras clave como `error`, `falla`, `API`, `null pointer`, `timeout`, `stack trace`, nombres de servicios, etc.
    - **Temporalidad:** Agrupar bugs reportados en un corto periodo de tiempo (ej. últimas 48 horas).

2.  **Identificación de Relaciones y Aislamiento:**
    - **Bugs Vinculados:** Usar `linkedIssues([ID])` para detectar relaciones explícitas (bloqueos, duplicados).
    - **Análisis de Aislados:** Los bugs sin relaciones aparentes deben ser destacados, ya que pueden representar problemas nuevos o no identificados.

3.  **Categorización Automática:**
    - **Críticos:** Issues sin resolver por más de 7 días con prioridad `High` o `Highest`.
    - **Clusters:** Grupos de 3 o más issues con alta similitud semántica o técnica.
    - **Aislados:** Issues que no encajan en ningún cluster pero requieren seguimiento.

4.  **Análisis de Tipologías de Error:**
    - **Extracción de Patrones:** Identificar patrones recurrentes en stack traces, logs y descripciones técnicas.
    - **Categorización de Errores:** Clasificar según tipologías técnicas (NullPointer, Database Timeout, Memory Leak, etc.).
    - **Correlación Técnica:** Establecer relaciones entre tipologías de error y componentes específicos.
    - **Análisis de Root Cause:** Inferir posibles causas raíz basadas en los patrones de error identificados.
    - **Priorización de Tipologías:** Ordenar tipos de errores por frecuencia, impacto y criticidad.
    
5.  **Mapa de Calor de Problemas:**
    - **Densidad por Componente:** Visualizar qué componentes concentran mayor número de errores técnicos.
    - **Evolución Temporal:** Analizar progresión de tipologías de error en el tiempo.
    - **Correlación con Deploys:** Identificar posibles relaciones entre releases y aparición de errores.

---

## 📊 FORMATO DE SALIDA OBLIGATORIO

### Resumen Ejecutivo Conciso
```markdown
## 📊 ANÁLISIS DE INCIDENCIAS: [PRODUCTO]
### ORIGEN: [TODOS/IOPPROSU/NO-IOPPROSU] | TOTAL: [N] INCIDENCIAS | [N] GRUPOS IDENTIFICADOS

### TIPOS DE INCIDENCIAS CRÍTICAS
| GRUPO | #Bugs | Tipología | Componente | Acción Principal |
|---------|-------|-----------|------------|------------------|
| [Nombre] | [N] | [NullPointer/Timeout/etc] | [API/Frontend/etc] | [Acción concreta] |
```

### Detalle por GRUPO
```markdown
### ⚠️ GRUPO: [NOMBRE] ([N] BUGS)
**Tipología:** [Categoría técnica del error]
**Patrón:** [Descripción concisa del patrón identificado, máx 2 líneas]
**IDs afectados:** [ID-1], [ID-2], [ID-3]... [+N más]

**Acción recomendada :**
[Acciones recomendadas y concretas]
```

---

## 🔄 CAPACIDADES ADICIONALES

### Análisis en Entorno de PRE-PRODUCCIÓN
- Para un análisis proactivo, ejecutar la misma JQL cambiando el entorno:
  `"Entorno Incidencia" = Preproduccion AND ...`

---

## 🎯 REGLAS DE ORO Y BUENAS PRÁCTICAS

### Reglas Prioritarias
- 🚨 **Exactitud Proyecto:** O no se pone proyecto o se usa IOPPROSU como nombre del proyecto, porque se ha especificado.
- 🚨 **Detección Automática:** Al mencionar IOPPROSU, aplicar automáticamente todas las reglas especiales (tipos, entornos).

### Reglas Generales
- ✅ **Enlaces a JIRA:** Cada issue mencionado debe incluir un enlace directo a la incidencia.
- ✅ **Evidencia Sólida:** Cada cluster o patrón identificado debe estar respaldado por evidencia extraída de las descripciones o campos de JIRA.
- ✅ **No Ignorar Aislados:** Los issues aislados son cruciales y deben ser reportados, ya que pueden representar problemas nuevos o no identificados.
- ✅ **Consistencia de Datos:** Validar que los datos obtenidos del MCP son coherentes antes de presentar el análisis.
- ⚠️ **No usar `project =`**: La búsqueda de productos debe hacerse exclusivamente a través de los campos personalizados definidos, excepto cuando se filtra específicamente por el proyecto IOPPROSU.
