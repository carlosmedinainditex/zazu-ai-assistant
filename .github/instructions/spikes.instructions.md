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

## 🎯 MISIÓN: EVALUACIÓN Y CLUSTERING DE SPIKES

### Activación Específica

#### Análisis de Spikes Sin Vinculación
**Triggers de activación:**
- "spikes huérfanos"
- "spikes sin vincular" 
- "spikes pendientes de vinculación"
- "spikes sin relación"
- "spikes de [PRODUCTO] sin vincular"
- "spikes de [PRODUCTO] en [PROYECTO] sin vincular"
- "spikes desconectados"

#### Análisis de Clústeres de Spikes
**Triggers de activación:**
- "clusteriza spikes de [PROYECTO]"
- "analiza clusteres de [PROYECTO]"
- "clustering spikes [PROYECTO]"
- "agrupa spikes de [PROYECTO]"
- "clústeres de spikes en [PROYECTO]"

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

#### Para Análisis de Spikes Sin Vinculación
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

#### Para Análisis de Clústeres de Spikes
- **Lógica de Búsqueda para Clustering:**
  - **Tipo de Incidencia:** `issuetype = Spike` (OBLIGATORIO)
  - **Estados Abiertos:** `AND status NOT IN (Discarded, Closed, Done)` (OBLIGATORIO) 
  - **Por Proyecto:** `AND project = "[PROYECTO]"` (OBLIGATORIO para clustering)
  - **Periodo Amplio:** `AND created >= -365d` (para obtener contexto suficiente)
  
- **JQL Base para Clustering:**
  ```jql
  issuetype = Spike AND status NOT IN (Discarded, Closed, Done) AND project = "[PROYECTO]" AND created >= -365d ORDER BY created DESC
  ```

- **Búsqueda Adaptativa:**
  - Si la JQL inicial no devuelve resultados, **ampliar el periodo** (`-365d` o eliminar restricción temporal)
  - Si aún no hay resultados, **verificar si existen spikes** con una JQL más genérica

### 3. Ejecución JQL y Extracción de Datos 
- **Comando:** Ejecutar la JQL construida utilizando el script principal con el modo de consulta directa:
  ```bash
  ./main.sh -q "JQL_CONSTRUIDA_ANTERIORMENTE"
  ```
  
  **🪟 IMPORTANTE PARA WINDOWS:**
  - **Escapar comillas dobles:** En Windows usar `\"` para comillas dentro de la JQL
  - **Comando Windows:** `./main.sh -q "issuetype = \"Spike\" AND \"Products/Enablers - Affected\" = \"PRODUCTO\""`
  - **Comando Unix/Linux (bash):** `./main.sh -q "issuetype = \"Spike\" AND \"Products/Enablers - Affected\" = \"PRODUCTO\""`
  - **Comando Unix/Linux (recomendado, usando comillas simples para evitar escapes):** `./main.sh -q 'issuetype = "Spike" AND "Products/Enablers - Affected" = "PRODUCTO"'`
  - **Nota:** En Unix/Linux, si usas comillas simples exteriores, no necesitas escapar las comillas dobles internas. Si usas bash, el ejemplo con `\"` también funciona, pero en otros shells puede variar.
  - **Problema común:** Las comillas dentro del JQL deben ser escapadas correctamente para evitar errores de parsing
  - **Alternativa Windows:** Usar comillas simples en JQL cuando sea posible: `./main.sh -q "issuetype = 'Spike' AND 'Products/Enablers - Affected' = 'PRODUCTO'"`
- **Proceso de Datos:** 
  - El script generará automáticamente un archivo JSON en `/reports/json/` con timestamp
  - **🚨 CRÍTICO:** Este archivo será la fuente de datos ÚNICA y AUTORITATIVA para el análisis

### 4. Recuperación y Validación de Contexto
- **Ubicación:** Buscar el archivo JSON más reciente por timestamp en `/reports/json/`
- **Carga:** Cargar COMPLETAMENTE todos los datos del archivo en el contexto de análisis
- **Verificación:** Confirmar que los datos son coherentes y completos antes de continuar

**Para Análisis Sin Vinculación:**
  ```
  ✅ Contexto cargado: [X] spikes sin vincular
  📊 Datos extraídos: [timestamp del archivo]
  🔍 Iniciando análisis profundo...
  ```

**Para Análisis de Clústeres:**
  ```
  ✅ Contexto cargado: [X] spikes del proyecto [PROYECTO]
  📊 Datos extraídos: [timestamp del archivo]
  🔬 Iniciando clustering temático...
  ```
---

## 🧠 ANÁLISIS DE SPIKES: DE DATOS A RECOMENDACIONES

### Metodología de Evaluación (Spikes Sin Vinculación)
1. **Análisis Simplificado:**
   - **Antigüedad:** Categorizar por tiempo transcurrido desde creación: crítico (>90d), medio (30-90d), reciente (<30d)
   - **Madurez Técnica:** Evaluar si el spike tiene conclusiones claras o hallazgos documentados
   - **Impacto Potencial:** Determinar relevancia para el producto/proyecto según descripción y comentarios

2. **Categorización Efectiva:**
   - **Alta Prioridad:** Spikes antiguos (>60 días) con hallazgos técnicos valiosos sin integrar
   - **Media Prioridad:** Spikes recientes con conclusiones claras pendientes de vincular
   - **Seguimiento:** Spikes en proceso que necesitan monitorización pero no acción inmediata

### Metodología de Clustering (Análisis Temático)
1. **Agrupación por Similitud Temática:**
   - **Análisis Semántico:** Agrupar spikes por palabras clave comunes en resúmenes y descripciones
   - **Patrones Técnicos:** Identificar tecnologías, arquitecturas o componentes recurrentes
   - **Dominios Funcionales:** Agrupar por áreas de negocio o funcionalidades similares
   - **Contexto de Investigación:** Identificar objetivos de investigación comunes (performance, integración, viabilidad, etc.)

2. **Factores de Clustering Obligatorios:**
   - **Products/Enablers Principal:** Campo `"Product/Enabler - Principal"` (customfield_43462)
   - **Products/Enablers Affected:** Campo `"Products/Enablers - Affected"` (customfield_43463)
   - **Términos Técnicos:** APIs, frameworks, arquitecturas mencionadas
   - **Área de Impacto:** Frontend, Backend, Infraestructura, Datos, etc.
   - **Temporalidad:** Spikes relacionados creados en periodos similares

3. **Identificación de Clústeres:**
   - **Mínimo 2 spikes** para formar un clúster válido
   - **Similitud semántica** >= 60% (basada en términos clave)
   - **Correlación de productos/enablers** cuando aplique
   - **Coherencia temporal** en investigaciones relacionadas

4. **Clasificación de Clústeres:**
   - **Críticos:** Clústeres con múltiples spikes antiguos (>90d) sin resolver
   - **Estratégicos:** Clústeres que afectan productos principales o múltiples enablers
   - **Operacionales:** Clústeres sobre herramientas, infraestructura o procesos
   - **Emergentes:** Clústeres de investigaciones recientes pero con alto potencial

5. **Síntesis de Clústeres:**
   - **Objetivo común:** Qué están investigando en conjunto
   - **Hallazgos clave:** Conclusiones principales ya documentadas
   - **Estado consolidado:** Progreso general del cluster
   - **Recomendaciones:** Acciones sugeridas para el conjunto

---

## 📊 FORMATO DE SALIDA

### Para Análisis de Spikes Sin Vinculación

#### Resumen Ejecutivo Optimizado
```markdown
## 📊 ANÁLISIS DE SPIKES SIN VINCULAR
### TOTAL: [N] SPIKES | ALTA PRIORIDAD: [N] | MEDIA PRIORIDAD: [N]

| Periodo | Cantidad | Estado |
|---------|----------|--------|
| > 90d | [N] | 🚨 |
| 30-90d | [N] | ⚠️ |
| < 30d | [N] | ✅ |
```

#### Listado por Prioridad
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

#### Detalle Técnico (Solo para Alta Prioridad)
```markdown
## 🔬 DETALLE: [ID]
**Spike:** [Resumen] | **Creado hace:** [N] días | **Estado:** [Estado]
**Hallazgos clave:** [1-2 conclusiones principales]
**Acción recomendada:** [Acción concreta: vincular/cerrar/convertir]
```

### Para Análisis de Clústeres de Spikes

#### Resumen Ejecutivo de Clustering
```markdown
## 🔬 ANÁLISIS DE CLÚSTERES: [PROYECTO]
### TOTAL: [N] SPIKES | [N] CLÚSTERES IDENTIFICADOS | [N] SPIKES AISLADOS

| Clasificación | Clústeres | Spikes | Criticidad |
|---------------|-----------|--------|------------|
| 🚨 Críticos | [N] | [N] | Alto impacto |
| 📋 Estratégicos | [N] | [N] | Productos clave |
| ⚙️ Operacionales | [N] | [N] | Infraestructura |
| 🌱 Emergentes | [N] | [N] | Nuevas líneas |
```

#### Detalle por Clúster
```markdown
### 🎯 CLÚSTER: [NOMBRE_TEMÁTICO] ([N] SPIKES) - [CLASIFICACIÓN]

**Temática Principal:** [Descripción concisa del tema común, máx 2 líneas]
**Productos/Enablers:** [Lista de productos afectados según customfields]
**Objetivo de Investigación:** [Qué están investigando en común]

**Spikes incluidos:**
- [ID-1]: [Resumen spike] | [Estado] | [Días]
- [ID-2]: [Resumen spike] | [Estado] | [Días]
- [ID-N]: [Resumen spike] | [Estado] | [Días]

**Hallazgos consolidados:**
[Síntesis de conclusiones principales extraídas de las descripciones]

**Estado del clúster:** [Progreso general: iniciado/en desarrollo/bloqueado/cerca de conclusión]

**Recomendaciones específicas:**
[Acciones concretas para el conjunto, considerando interdependencias]

---
```

#### Spikes Aislados
```markdown
### 🔍 SPIKES AISLADOS ([N])
| ID | Resumen | Producto/Enabler | Días | Estado | Prioridad |
|----|---------|------------------|------|--------|-----------|
| [ID-1] | [Resumen max 50 chars] | [Producto] | [N] | [Estado] | [🚨/⚠️/✅] |
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

### 🪟 Compatibilidad Multiplataforma
**CRÍTICO - Manejo de Caracteres Especiales en Windows:**
- **Regla fundamental:** En Windows, SIEMPRE escapar comillas dobles dentro de JQL usando `\"`
- **Sintaxis correcta Windows:** `./main.sh -q "issuetype = \"Spike\" AND \"Products/Enablers - Affected\" = \"PRODUCTO\""`
- **Sintaxis correcta Unix/Linux:** `./main.sh -q "issuetype = \"Spike\" AND \"Products/Enablers - Affected\" = \"PRODUCTO\""`
- **Alternativa universal:** Usar comillas simples cuando sea posible: `./main.sh -q "issuetype = 'Spike'"`
- **Error común:** `./main.sh -q "issuetype = "Spike""` → **INCORRECTO** - causará fallos de parsing
- **Verificación:** Si el comando falla, revisar primero el escape de comillas antes que la sintaxis JQL

### Reglas Prioritarias
- 🚨 **Verificación de Enlaces:** Asegurar que se está usando correctamente `linkedIssuesOf IS EMPTY` para detectar spikes sin relaciones.
- 🚨 **Exclusión de Estados:** SIEMPRE excluir `Discarded` y `Closed` de la búsqueda.
- 🚨 **Clustering Obligatorio:** Para análisis de clústeres, NO filtrar por `linkedIssuesOf IS EMPTY` - incluir todos los spikes abiertos.
- 🚨 **Customfields Críticos:** En clustering, SIEMPRE considerar los campos `"Product/Enabler - Principal"` y `"Products/Enablers - Affected"` como factores de agrupación.

### Reglas Generales
- ✅ **Enlaces a JIRA:** Cada spike mencionado debe incluir un enlace directo al ticket.
- ✅ **Evidencia en Recomendaciones:** Las recomendaciones deben basarse en contenido real extraído del spike.
- ✅ **Priorización por Antigüedad:** Los spikes más antiguos deben recibir mayor atención y análisis detallado.
- ✅ **Contextualización Técnica:** Relacionar el contenido del spike con posibles implementaciones o decisiones arquitectónicas.
- ✅ **Síntesis de Clústeres:** En análisis de clustering, proporcionar una síntesis explicativa clara de cada clúster identificado.
- ✅ **Correlación Productos:** Usar los customfields de productos como elemento clave para validar la coherencia de los clústeres.
- ⚠️ **No Asumir Implementación:** Las recomendaciones deben enfocarse en la vinculación, no en detalles técnicos de implementación que no se mencionen en el spike.
