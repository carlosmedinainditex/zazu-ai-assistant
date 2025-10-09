---
applyTo: "**"
description: "Instrucciones clave para el análisis de Spikes con el agente IA de Zazu (zazu-jira-api-connector), herramienta especializada en la evaluación de investigaciones técnicas en JIRA con integración MCP Atlassian."
author: Carlos Medina
version: 2.0
tags: ["zazu", "jira", "api", "automatizacion", "analisis", "spikes", "investigacion", "atlassian", "mcp", "ai-agent"]
tools: ["atlassian", "geppetto-api", "geppeto", "github"]
globs: ["**/zazu-jira-api-connector/**/*", "**/*zazu*", "**/reports/**/*"]
---

# 🚨 INSTRUCCIONES ESPECÍFICAS - ANÁLISIS DE SPIKES ZAZU
- Nunca uses Search de JIRA con MCP

## 🎯 MISIÓN: EVALUACIÓN DE SPIKES SIN VINCULACIÓN

### Activación Específica
**Triggers de activación:**
- "spikes huérfanos"
- "spikes sin vincular" 
- "spikes pendientes de vinculación"
- "spikes sin relación"
- "spikes de [PRODUCTO] sin vincular"
- "spikes de [PRODUCTO] en [PROYECTO] sin vincular"
- "spikes desconectados"

---

## 🔍 FLUJO DE EJECUCIÓN OBLIGATORIO

### 1. Mapeo y Validación de Parámetros
- **Mapeo de Producto:** 
  - El parámetro `[PRODUCTO]` debe mapearse al campo Jira `"Products/Enablers - Affected"` (customfield_43463).
  - También verificar contra `"Product/Enabler - Principal"` (customfield_43462).
  - **Procedimiento MCP:** Ejecutar `mcp_atlassian_jira_search_fields keyword="[PRODUCTO]"` para confirmar existencia.

- **Mapeo de Proyecto:** 
  - El parámetro `[PROYECTO]` (ej: IOPPROSU) debe mapearse al campo Jira `project`.
  - **Procedimiento MCP:** Verificar que el proyecto existe antes de incluirlo en la consulta.

- **Resultado de validación:**
  - **✅ Éxito:** Si se encuentran los parámetros, continuar.
  - **❌ Fracaso:** Si no se encuentran, notificar: `No se encontró el [PRODUCTO/PROYECTO]. Por favor, verifique el nombre o ID.`.

### 2. Construcción JQL
- **Lógica de Búsqueda:**
  - **Tipo de Incidencia:** `issuetype = Spike` (OBLIGATORIO)
  - **Filtro de Relaciones:** `AND linkedIssuesOf IS EMPTY` (OBLIGATORIO) 
  - **Estados a Excluir:** `AND status NOT IN (Discarded, Closed)` (OBLIGATORIO)
  - **Filtrados opcionales:**
    - **Por Producto:** `AND ("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]")`
    - **Por Proyecto:** `AND project = "[PROYECTO]"` 
  - **Periodo:** `AND created >= -180d` (modificable según necesidad)
  
- **JQL Base (General):**
  ```jql
  issuetype = Spike AND linkedIssuesOf IS EMPTY AND status NOT IN (Discarded, Closed) ORDER BY created DESC
  ```
  
- **JQL Base (Producto y Proyecto):**
  ```jql
  issuetype = Spike AND linkedIssuesOf IS EMPTY AND status NOT IN (Discarded, Closed) AND ("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]") AND project = "[PROYECTO]" ORDER BY created DESC
  ```

- **Búsqueda Adaptativa:**
  - Si la JQL inicial no devuelve resultados, **ampliar el periodo** (`-365d` o eliminar restricción temporal)
  - Si aún no hay resultados, **verificar si existen spikes** con una JQL más genérica

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
  ✅ Contexto cargado: [X] spikes sin vincular
  📊 Datos extraídos: [timestamp del archivo]
  🔍 Iniciando análisis profundo...
  ```
---

## 🧠 ANÁLISIS DE SPIKES: DE DATOS A RECOMENDACIONES

### Metodología de Evaluación
1. **Análisis Simplificado:**
   - **Antigüedad:** Categorizar por tiempo transcurrido desde creación: crítico (>90d), medio (30-90d), reciente (<30d)
   - **Madurez Técnica:** Evaluar si el spike tiene conclusiones claras o hallazgos documentados
   - **Impacto Potencial:** Determinar relevancia para el producto/proyecto según descripción y comentarios

2. **Categorización Efectiva:**
   - **Alta Prioridad:** Spikes antiguos (>60 días) con hallazgos técnicos valiosos sin integrar
   - **Media Prioridad:** Spikes recientes con conclusiones claras pendientes de vincular
   - **Seguimiento:** Spikes en proceso que necesitan monitorización pero no acción inmediata

---

## 📊 FORMATO DE SALIDA SIMPLIFICADO

### Resumen Ejecutivo Optimizado
```markdown
## 📊 ANÁLISIS DE SPIKES SIN VINCULAR
### TOTAL: [N] SPIKES | ALTA PRIORIDAD: [N] | MEDIA PRIORIDAD: [N]

| Periodo | Cantidad | Estado |
|---------|----------|--------|
| > 90d | [N] | 🚨 |
| 30-90d | [N] | ⚠️ |
| < 30d | [N] | ✅ |
```

### Listado por Prioridad
```markdown
### 🚨 ALTA PRIORIDAD ([N])
| ID | Resumen | Días | Estado | Acción |
|----|---------|------|--------|--------|
| [ID-1] | [Resumen max 60 chars] | [N] | [Estado] | [Acción corta] |

### ⚠️ MEDIA PRIORIDAD ([N])
| ID | Resumen | Días | Estado | Acción |
|----|---------|------|--------|--------|
| [ID-1] | [Resumen max 60 chars] | [N] | [Estado] | [Acción corta] |
```

### Detalle Técnico (Solo para Alta Prioridad)
```markdown
## 🔬 DETALLE: [ID]
**Spike:** [Resumen] | **Creado hace:** [N] días | **Estado:** [Estado]
**Hallazgos clave:** [1-2 conclusiones principales]
**Acción recomendada:** [Acción concreta: vincular/cerrar/convertir]
```

---

## 🔄 CAPACIDADES ADICIONALES

### Filtrado por Proyecto
- Permitir filtrado específico por proyecto usando la sintaxis:
  ```jql
  ... AND project = "[PROYECTO]"
  ```

### Análisis Combinado
- Permitir filtrado combinado de producto y proyecto:
  ```jql
  ... AND ("Products/Enablers - Affected" = "[PRODUCTO]") AND project = "[PROYECTO]"
  ```

---

## 🎯 REGLAS DE ORO Y BUENAS PRÁCTICAS

### Reglas Prioritarias
- 🚨 **Verificación de Enlaces:** Asegurar que se está usando correctamente `linkedIssuesOf IS EMPTY` para detectar spikes sin relaciones.
- 🚨 **Exclusión de Estados:** SIEMPRE excluir `Discarded` y `Closed` de la búsqueda.

### Reglas Generales
- ✅ **Enlaces a JIRA:** Cada spike mencionado debe incluir un enlace directo al ticket.
- ✅ **Evidencia en Recomendaciones:** Las recomendaciones deben basarse en contenido real extraído del spike.
- ✅ **Priorización por Antigüedad:** Los spikes más antiguos deben recibir mayor atención y análisis detallado.
- ✅ **Contextualización Técnica:** Relacionar el contenido del spike con posibles implementaciones o decisiones arquitectónicas.
- ⚠️ **No Asumir Implementación:** Las recomendaciones deben enfocarse en la vinculación, no en detalles técnicos de implementación que no se mencionen en el spike.
