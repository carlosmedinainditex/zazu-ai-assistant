---
applyTo: "**"
description: "Instrucciones clave para el análisis de Spikes con el agente IA de Zazu (zazu-jira-api-connclaeconnectrovector), herramienta especializada en la evaluación de investigaciones técnicas en JIRA con integración MCP Atlassian."
author: Carlos Medina
version: 1.0
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
- "spikes desconectados"

---

## 🔍 FLUJO DE EJECUCIÓN OBLIGATORIO

### 1. Validación de Producto (Opcional)
- **Entrada:** Si se proporciona `[PRODUCTO]`, validar su existencia vía MCP.
  - **Campos a verificar:** `"Products/Enablers - Affected"` (customfield_43463) y `"Product/Enabler - Principal"` (customfield_43462).
  - **Comando:** ``"Product/Enabler - Principal"` = "[PRODUCTO]"`
- **Resultado:**
  - **✅ Éxito:** Si se encuentra el producto, continuar al siguiente paso.
  - **❌ Fracaso:** Si no se encuentra, **detener ejecución** y notificar al usuario: `No se encontró el producto "[PRODUCTO]". Por favor, verifique el nombre o ID.`.
- **Sin producto:** Si no se especifica un producto, realizar búsqueda general de spikes.

### 2. Construcción JQL
- **Lógica de Búsqueda:**
  - **Tipo de Incidencia:** `issuetype = Spike` (OBLIGATORIO)
  - **Filtro de Relaciones:** `AND linkedIssuesOf IS EMPTY` (OBLIGATORIO) 
  - **Estados a Excluir:** `AND status NOT IN (Discarded, Closed)` (OBLIGATORIO)
  - **Filtrado por Producto (opcional):**
    - Si se especifica producto: `AND ("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]")`
  - **Periodo (opcional):** `AND created >= -180d` (modificable según necesidad)
  
- **JQL Base (General):**
  ```jql
  issuetype = Spike AND linkedIssuesOf IS EMPTY AND status NOT IN (Discarded, Closed) ORDER BY created DESC
  ```
  
- **JQL Base (Con Producto):**
  ```jql
  issuetype = Spike AND linkedIssuesOf IS EMPTY AND status NOT IN (Discarded, Closed) AND ("Products/Enablers - Affected" = "[PRODUCTO]" OR "Product/Enabler - Principal" = "[PRODUCTO]") ORDER BY created DESC
  ```

- **Búsqueda Adaptativa:**
  - Si la JQL inicial no devuelve resultados, **ampliar el periodo** (`-365d` o eliminar restricción temporal)
  - Si aún no hay resultados, **verificar si existen spikes** para ese producto con otra JQL más genérica

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
1. **Análisis de Madurez:**
   - **Tiempo Activo:** Calcular días transcurridos desde creación (`created`) hasta hoy.
   - **Estado Actual:** Priorizar análisis por estado (`In Progress` > `Review` > `Done` > otros).
   - **Actividad Reciente:** Evaluar comentarios o actualizaciones en últimos 30 días.

2. **Evaluación de Contenido:**
   - **Descripción:** Analizar si contiene objetivos claros, preguntas a responder y criterios de éxito.
   - **Comentarios:** Buscar evidencia de conclusiones, hallazgos o decisiones técnicas.
   - **Anexos:** Verificar presencia de documentación técnica, POCs o diagramas.

3. **Categorización por Impacto:**
   - **Críticos:** Spikes activos por más de 30 días sin vinculación ni conclusiones documentadas.
   - **Relevantes:** Spikes con hallazgos valiosos pero sin integrar a iniciativas/épicas.
   - **Completos:** Spikes con conclusiones claras que deberían vincularse a tickets de implementación.
   
4. **Recomendación de Vinculación:**
   - **Análisis de Resumen/Descripción:** Identificar palabras clave que indiquen área funcional/técnica.
   - **Matching con Iniciativas Activas:** Sugerir posibles iniciativas/épicas relacionadas.
   - **Acción Recomendada:** Proponer si debe vincularse, cerrarse o convertirse en una épica/historia.

---

## 📊 FORMATO DE SALIDA OBLIGATORIO

### Resumen Ejecutivo Conciso
```markdown
## 📊 ANÁLISIS DE SPIKES SIN VINCULAR
### TOTAL: [N] SPIKES | CRÍTICOS: [N] | RELEVANTES: [N] | COMPLETOS: [N]

### RESUMEN POR ANTIGÜEDAD
| Periodo | Cantidad | % del Total |
|---------|----------|------------|
| > 90 días | [N] | [X]% |
| 30-90 días | [N] | [X]% |
| < 30 días | [N] | [X]% |
```

### Detalle por Categoría
```markdown
### ⚠️ SPIKES CRÍTICOS ([N])
| ID | Resumen | Días | Estado | Recomendación |
|----|---------|------|--------|--------------|
| [ID-1] | [Resumen] | [Días] | [Estado] | [Acción recomendada] |

### 🔍 SPIKES RELEVANTES ([N])
| ID | Resumen | Días | Estado | Recomendación |
|----|---------|------|--------|--------------|
| [ID-1] | [Resumen] | [Días] | [Estado] | [Acción recomendada] |

### ✅ SPIKES COMPLETOS ([N])
| ID | Resumen | Días | Estado | Recomendación |
|----|---------|------|--------|--------------|
| [ID-1] | [Resumen] | [Días] | [Estado] | [Acción recomendada] |
```

### Análisis Detallado (Para Críticos)
```markdown
## 🔬 DETALLE DE SPIKE: [ID]
**Resumen:** [Resumen del spike]
**Creado:** [Fecha de creación] ([N] días)
**Estado:** [Estado actual]
**Última actividad:** [Fecha último comentario/cambio]

**Hallazgos encontrados:**
- [Hallazgo 1 identificado en descripción/comentarios]
- [Hallazgo 2 identificado en descripción/comentarios]

**Posibles vinculaciones:**
- [Iniciativa/Épica relacionada 1]
- [Iniciativa/Épica relacionada 2]

**Recomendación:**
[Acción recomendada con justificación específica]
```

---

## 🔄 CAPACIDADES ADICIONALES

### Búsqueda por Equipos o Proyectos
- Permitir filtrado adicional por equipo de desarrollo:
  ```jql
  ... AND "Team" = "[EQUIPO]"
  ```

### Análisis de Tendencias
- Identificar equipos o áreas con mayor incidencia de spikes sin vincular
- Calcular tiempo promedio de resolución y vinculación por equipo/área

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
