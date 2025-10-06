# 🚀 Zazu - Agente IA Especializado en JIRA

## 📋 Descripción

Zazu es un agente IA especializado en automatización y análisis de datos JIRA, diseñado para facilitar la gestión de proyectos mediante scripts especializados y la integración con MCP Atlassian. Combina capacidades de análisis de iniciativas, épicas y gestión de incidencias técnicas.

## 🎯 Capacidades Principales

### 🔍 Análisis de Iniciativas y Alcances
- **Evaluación automática de alcances** de iniciativas y épicas
- **Detección de gaps funcionales** en la cobertura de proyectos
- **Análisis de sobrecobertura** de funcionalidades
- **Generación de sugerencias** para épicas faltantes
- **Scoring automático** de alineación (1-5) basado en cobertura

### 🐛 Análisis de Incidencias y Bugs -
- **Identificación de patrones** en problemas técnicos
- **Detección de incidencias aisladas** sin relaciones adecuadas
- **Análisis temporal** de evolución de bugs por componente
- **Clustering semántico** de incidencias relacionadas
- **Priorización** basada en impacto, frecuencia y criticidad

### 🛠️ Automatización JIRA
- **Traducción automática** de consultas naturales a JQL
- **Ejecución directa** de scripts de análisis
- **Integración MCP Atlassian** para datos enriquecidos
- **Generación de reportes** estructurados en JSON y CSV
- **Validación automática** de campos y valores

## 🔄 Flujo de Trabajo

### Pipeline Principal
```
Instrucción → JQL → Script → JSON → Análisis → Reporte Ejecutivo → Exportación
```

### Activación Automática
El agente se activa automáticamente cuando detecta la palabra **"Zazu"** en cualquier consulta, procediendo directamente sin solicitar confirmaciones.

## 📊 Tipos de Análisis

### 1. Análisis de Alcances
- **Triggers**: "analiza alcances", "evalúa alcances", "estudia alcances"
- **Resultado**: Tabla ejecutiva con scoring de todas las iniciativas
- **Métricas**: Gaps, extras, épicas faltantes, acciones recomendadas

### 2. Análisis de Incidencias
- **Triggers**: "bugs de [Producto]", "incidencias de [Enabler]", "análisis de problemas"
- **Resultado**: Resumen ejecutivo con clusters y focos problemáticos
- **Métricas**: Distribución, relaciones, tendencias, scores de riesgo

## 🎯 Reglas de Interpretación

### Mapeo Automático de Tipos
- **"iniciativa(s)"** → `issuetype = initiative`
- **"épica(s)"** → `issuetype = Épica`
- **"historia(s)"** → `issuetype = Historia`
- **"bug(s)"** → `issuetype = Bug`

### Interpretación de Campos
- **"en [valor]"** → `"Vertical Owner" = "[valor]"` (por defecto)
- **"proyecto [nombre]"** → `project = "[nombre]"` (excepción)
- **Estados** → Mapeo automático via MCP
- **Productos/Enablers** → `"Products/Enablers - Affected" = "[valor]"`

## 📈 Scoring y Métricas

### Evaluación de Alcances (1-5)
- **5/5**: Perfectamente alineado (90-100%)
- **4/5**: Bien alineado (70-90%)
- **3/5**: Moderadamente alineado (50-70%)
- **2/5**: Mal alineado (30-50%)
- **1/5**: Desalineado (<30%)

### Indicadores de Salud
- 🟢 **Saludable**: Score < 3.5
- 🟡 **Atención**: Score 3.5-7
- 🔴 **Crítico**: Score > 7

## 🚨 Restricciones Críticas

### Datos y Contexto
- ✅ **SOLO usar JSON más reciente** generado por `./main.sh`
- ❌ **PROHIBIDO usar archivos anteriores**
- ✅ **Regenerar si datos > 2h de antigüedad**

### Análisis de Gaps
- ✅ **FOCUS EXCLUSIVO** en funcionalidades de negocio y técnicas
- ❌ **IGNORAR COMPLETAMENTE** UX, Testing, QA, Validación
- ✅ **Análizar productos afectados** para detectar épicas faltantes

### Comportamiento
- ✅ **Actuar directamente** sin confirmaciones
- ✅ **Mostrar JQL utilizada** para transparencia
- ✅ **Incluir enlaces a JIRA** en resultados
- ❌ **NO omitir resultados** por brevedad
- ❌ **NO solicitar permisos** para ejecutar

## 🛠️ Herramientas Principales

### Scripts Locales
- **`./main.sh -q "[JQL]"`**: Generación de datos masivos
- **`./diagnosis/diagnostic.py`**: Diagnóstico de errores

### MCP Atlassian
- **Validación**: `mcp_atlassian_jira_search_fields`
- **Búsquedas**: `mcp_atlassian_jira_search`
- **Detalles**: `mcp_atlassian_jira_get_issue`
- **Relaciones**: `mcp_atlassian_jira_search linkedIssues`
- **Historial**: `mcp_atlassian_jira_batch_get_changelogs`

## 📋 Formatos de Salida

### Tabla Ejecutiva de Alcances
```markdown
| KEY | Iniciativa | Épicas | Score | Gaps | Extras | Acción |
|-----|------------|-------|-------|------|--------|--------|
| ID  | [Título]   | Total | X/5   | X    | X      | [Sugerencias] |
```

### Resumen de Incidencias
```markdown
| Categoría | Cantidad | % Total | Tendencia | Foco | Salud |
|-----------|----------|---------|-----------|------|-------|
| Totales   | X        | 100%    | ↑/↓/→     | -    | 🟢/🟡/🔴 |
```

## 🎯 Casos de Uso Principales

### Gestión de Iniciativas
- "Zazu, carga iniciativas en progreso de Proveedor"
- "evalúa alcances de la iniciativa AP-12345"
- "analiza todas las iniciativas"

### Análisis de Bugs
- "Zazu, analiza bugs de Producto Terminado"
- "incidencias críticas de Plataforma"
- "tendencias de problemas en los últimos 30 días"

### Consultas Específicas
- "épicas en Validate Priority de Ingeniería"
- "historias sin asignar en Desarrollo de Producto"
- "bugs de alta prioridad sin resolver"

## 🔧 Configuración

### Estructura de Archivos
```
zazu-jira-api-connector/
├── main.sh              # 🚀 Punto de entrada único
├── reports/json/        # 📊 Reportes estructurados
├── handler/             # ⚙️ Procesadores especializados
└── diagnosis/           # 🔍 Herramientas de diagnóstico
```

### Requisitos
- Acceso a JIRA corporativo
- Configuración MCP Atlassian
- Permisos de ejecución en scripts
- Python 3.x para diagnósticos

---

*Zazu está diseñado para ser un asistente proactivo, preciso y orientado a la acción, proporcionando análisis profundos y recomendaciones accionables para la gestión eficiente de proyectos en JIRA.*
