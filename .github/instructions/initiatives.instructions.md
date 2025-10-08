---
applyTo: "**"
description: Instrucciones para el agente IA de Zazu (zazu-jira-api-connector), herramienta de automatización y análisis de JIRA con integración MCP Atlassian.
author: Carlos Medina
version: 4.0
tags: ["zazu", "jira", "api", "automatizacion", "analisis", "atlassian", "mcp", "ai-agent"]
tools: ["atlassian", "geppetto-api", "geppeto", "github"]
globs: ["**/zazu-jira-api-connector/**/*", "**/*zazu*", "**/reports/**/*"]
---

# 🚨 INSTRUCCIONES ESPECÍFICAS - ANÁLISIS DE ALCANCES ZAZU

## 🎯 ESPECIALIZACIÓN EN INICIATIVAS Y ÉPICAS

### Activación Específica
**Triggers específicos para análisis de alcances:**
- "analiza alcances"
- "evalúa alcances" 
- "estudia alcances"
- "mejoras sobre los alcances"
- "qué falta" / "gaps"

---

## 🔄 FLUJO DE TRABAJO OBLIGATORIO

### 1. Verificación de Contexto
**REGLA CRÍTICA DE DATOS:**
- 🚨 **Usar ÚNICAMENTE el archivo JSON más reciente** generado por `./main.sh`
- ❌ **PROHIBIDO contemplar archivos anteriores**
- ✅ **Verificar timestamp del último reporte** en `/reports/json/`

### 2. Traducción JQL Automática

#### Tipos de Issue
- **"iniciativa(s)"** → `issuetype = initiative`
- **"épica(s)"** → `issuetype = Épica` (NUNCA "Epic")
- **"historia(s)"** → `issuetype = Historia`
- **"tarea(s)"** → `issuetype = Tarea`
- **"bug(s)"** → `issuetype = Bug`

#### Campos Críticos
- **Propietario** → `"Vertical Owner" = "[valor]"`
- **Afectado** → `"Affected Product Verticals" = "[valor]"`
- **Estado** → `status = '[valor]'`
- **Prioridad** → `priority = '[valor]'`

#### Regla Crítica de Búsqueda "EN"
**🚨 INTERPRETACIÓN AUTOMÁTICA OBLIGATORIA DE "EN [valor]":**

**REGLA PRINCIPAL (99% de los casos):**
- ✅ **SIEMPRE POR DEFECTO:** `"en [valor]"` → `"Vertical Owner" = "[valor]"`
- ✅ **APLICAR AUTOMÁTICAMENTE** sin confirmación
- ✅ **NO PREGUNTAR** al usuario por clarificación

**ÚNICA EXCEPCIÓN (1% de los casos):**
- ⚠️ **SOLO cuando se menciona EXPLÍCITAMENTE "proyecto"** → `project = "[nombre]"`
- ⚠️ **Requiere uso literal de la palabra "proyecto"**

**🔍 ALGORITMO DE DECISIÓN:**
1. **¿Contiene "proyecto" + nombre?** → Buscar por `project`
2. **¿Solo dice "en [valor]"?** → **SIEMPRE** usar `"Vertical Owner" = "[valor]"`
3. **¿Hay dudas?** → **SIEMPRE** usar `"Vertical Owner"` (comportamiento por defecto)

**✅ EJEMPLOS CORRECTOS (Vertical Owner):**
- "iniciativas en Proveedor" → `"Vertical Owner" = "Proveedor"`
- "épicas en Producto Terminado" → `"Vertical Owner" = "Producto Terminado"`
- "historias en Ingeniería" → `"Vertical Owner" = "Ingeniería"`
- "tareas en Materias Primas" → `"Vertical Owner" = "Materias Primas"`
- "bugs en Desarrollo de Producto" → `"Vertical Owner" = "Desarrollo de Producto"`
- "issues en Dirección" → `"Vertical Owner" = "Dirección y Planificación"`
- "épicas en Plataforma" → `"Vertical Owner" = "Plataforma"`

**🔀 EJEMPLOS DE EXCEPCIÓN (Project):**
- "tareas en **proyecto** Dashboard y Producto" → `project = "AP-Production"`
- "bugs en **el proyecto** Mobile" → `project = "AP-Collaborator Mobile"`  
- "épicas **del proyecto** Portal" → `project = "AP-Purchase Extranet Migration"`

**⚠️ PALABRAS CLAVE EXACTAS PARA ACTIVAR BÚSQUEDA POR PROJECT:**
- "proyecto [nombre]"
- "el proyecto [nombre]"
- "del proyecto [nombre]"
- "en proyecto [nombre]"

**🚨 REGLA DE ORO:**
- **Sin "proyecto" explícito** → **SIEMPRE** `"Vertical Owner"`
- **Con "proyecto" explícito** → `project`
- **En caso de duda** → **SIEMPRE** `"Vertical Owner"`

#### Estados - Mapeo Automático MCP
**🚨 PROCEDIMIENTO:**
1. Usuario menciona estado → **EJECUTAR MCP:** `jira_search_fields keyword="[término]"`
2. **USAR valor exacto** en JQL → **APLICAR automáticamente**

**Mapeo automático:**
- discovery → `status = 'Discovering'`
- análisis → `status = 'Analyzing'`
- progreso → `status = 'In Progress'`
- revisión → `status = 'Review'`
- hecho → `status = 'Done'`

### 3. Ejecución Directa
**COMANDO ÚNICO:**
```bash
./main.sh -q "consulta_JQL_generada"
```

### 4. Procesamiento Automático
1. **Leer JSON más reciente** por timestamp
2. **Cargar en contexto** todos los datos
3. **Validar integridad** de información
4. **Confirmar carga:**
   ```
   ✅ Contexto cargado: [X] elementos ([tipo])
   📊 Datos desde: [timestamp]
   � Iniciando análisis automático...
   ```



---

## 🧠 CAPACIDADES DE ANÁLISIS
## 🎯 ANÁLISIS ESPECIALIZADO: EVALUACIÓN DE ALCANCES

### Activación y Ejecución Inmediata
**Triggers que ejecutan automáticamente SIN confirmación:**
- "analiza alcances" → **EJECUCIÓN INMEDIATA**
- "evalúa alcances" → **EJECUCIÓN INMEDIATA**
- "estudia alcances" → **EJECUCIÓN INMEDIATA**
- "mejoras sobre los alcances" → **ANÁLISIS DETALLADO AUTOMÁTICO**
- "qué falta" / "gaps" → **ANÁLISIS DE COBERTURA DIRECTO**

### Flujo de Análisis Detallado

#### 1. Recopilación de Datos
**🚨 OBLIGATORIO - Consultar Descripciones MCP Atlassian si no están en JSON:**

**Para cada iniciativa:**
3. **Procesar descripciones para identificar:**
   - Objetivos estratégicos y de negocio
   - Funcionalidades específicas requeridas
   - Criterios de aceptación definidos
   - Alcance técnico y funcional
   - Componentes y módulos involucrados
   - Dependencias externas mencionadas

**⚠️ CRITICAL:** Las descripciones contienen la información más detallada sobre el verdadero alcance. **NO analizar alcances sin consultar descriptions via MCP.**

Si las Épicas no tienen descripción, es un 0/5 el score.
Si no hay épicas hijas, es un 0/5 en el score
NO muestres tablas parciales, siempre una tabla con todos los datos completos

## 🎯 RESTRICCIONES CRÍTICAS PARA ANÁLISIS DE ALCANCES

### 🚨 RESTRICCIÓN INFRACOBERTURAS
- ✅ **SOLO** analizar áreas **FUNCIONALES** no cubiertas
- ❌ **IGNORAR COMPLETAMENTE**: UX, Validación, Pruebas, Testing, QA
- ✅ **FOCUS EXCLUSIVO**: Funcionalidades negocio, Componentes técnicos, APIs

###  RESTRICCIÓN SOBRECOBERTURAS  
- ✅ **SOLO** detectar funcionalidades **BUSINESS/TÉCNICAS** extra
- ❌ **IGNORAR COMPLETAMENTE**: UX, Validación, Pruebas, Testing, QA
- ✅ **FOCUS EXCLUSIVO**: Desarrollos adicionales negocio, Componentes extra

### Reglas de Scoring
- **Sin épicas hijas** = 0/5
- **Épicas sin descripción** = 0/5  
- **Productos afectados > épicas** = Gap crítico

## 📊 EVALUACIÓN AUTOMÁTICA Y FORMATO

### Scoring de Alineación (1-5)
- **5/5**: Perfectamente alineado (90-100%)
- **4/5**: Bien alineado (70-90%)
- **3/5**: Moderadamente alineado (50-70%)
- **2/5**: Mal alineado (30-50%)
- **1/5**: Desalineado (<30%)

### Formato Obligatorio
```markdown
| KEY | Iniciativa | Épicas | Score | Gaps | Extras | Acción |
|-----|------------|-------|------|--------|---------|--------|
| ID  | [Título]  | Total | X/5  | X      | X       | [Sugerencias] |
```

### Estructura JSON Iniciativa
- **Campos críticos:** `id`, `summary`, `description`, `children`
- **Épicas hijas:** Array en campo `children` con `summary` y `description`

## 🎯 REGLAS ESPECÍFICAS PARA ALCANCES

### Obligatorio en Análisis de Alcances
- ✅ **Consultar descripciones vía MCP** si no están en JSON
- ✅ **Tabla completa SIEMPRE** - nunca parcial
- ✅ **Usar ÚNICAMENTE datos frescos** (< 2h)
- ✅ **Focus SOLO funcional** - ignorar UX/Testing
- ✅ **Seguir formato tabla exacto** - no modificar

### Ejemplo de Estructura JSON
```JSON
{
  "id": "ID_INICIATIVA",
  "summary": "TITULO_INICIATIVA", 
  "description": "DESCRIPCION_INICIATIVA",
  "children": [
    {
      "id": "ID_EPICA",
      "summary": "TITULO_EPICA",
      "description": "DESCRIPCION_EPICA"
    }
  ]
}
```
