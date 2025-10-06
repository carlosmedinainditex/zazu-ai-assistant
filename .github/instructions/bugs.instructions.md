---
applyTo: "**"
description: Instrucciones para el análisis de incidencias con el agente IA de Zazu (zazu-jira-api-connector), herramienta especializada en análisis de bugs y problemas en JIRA con integración MCP Atlassian.
author: Carlos Medina
version: 1.3
tags: ["zazu", "jira", "api", "automatizacion", "analisis", "bugs", "incidencias", "atlassian", "mcp", "ai-agent"]
globs: ["**/zazu-jira-api-connector/**/*", "**/*zazu*", "**/reports/**/*"]
---

# 🚨 INSTRUCCIONES ESPECÍFICAS - ANÁLISIS DE INCIDENCIAS ZAZU

## 🎯 ESPECIALIZACIÓN EN BUGS Y PROBLEMAS TÉCNICOS

### Activación Específica
**Triggers específicos para análisis de incidencias:**
- "bugs de [Producto/Enabler]"
- "incidencias de [componente]"
- "análisis de problemas técnicos"
- "tendencias de incidencias"

---

## � CONSTRUCCIÓN JQL ESPECÍFICA PARA BUGS

### Configuración de Búsqueda de Incidencias
- **Tipo obligatorio:** `issuetype = Bug`
- **Campo principal:** `"Products/Enablers - Affected" = "[valor]"` (customfield_43463)
- **Periodo por defecto:** `AND created >= -30d`
- **Ordenación crítica:** `ORDER BY priority DESC, created DESC`
- **🚨 NUNCA usar** `project = "[Proyecto]"` para bugs

---

## � MCP ESPECÍFICO PARA ANÁLISIS DE INCIDENCIAS

### Comandos Especializados en Bugs
- **Análisis de relaciones:** `mcp_atlassian_jira_search jql="key in linkedIssues([ID])"`
- **Historial de cambios:** `mcp_atlassian_jira_batch_get_changelogs issue_ids_or_keys=["ID1","ID2"]`
- **Búsqueda por texto:** `jql="'Products/Enablers - Affected' = '[valor]' AND text ~ '[keyword]'"`
- **Filtro por componente:** `jql="component = '[componente]' AND issuetype = Bug"`
- **Actividad reciente:** `jql="status changed AFTER -7d AND issuetype = Bug"`

---

## 🧠 ANÁLISIS DE INCIDENCIAS

### Regla Crítica de Interpretación
🚨 **SIEMPRE interpretar [Producto/Enabler] como valor para campo "Products/Enablers - Affected"**

### Procedimiento Analítico
1. **Incidencias aisladas:**
   - Identificar tickets sin relaciones (`linkedIssues([ID])` vacío)
   - Catalogar por componente/módulo y prioridad
   - Aplicar NLP para análisis semántico de similitudes en descripciones
   - Calcular score de aislamiento basado en edad y prioridad del ticket
   
2. **Análisis de relaciones:**
   - Buscar similitudes entre incidencias aisladas (texto, componente, reportador)
   - Identificar clusters de problemas relacionados (grafo de relaciones)
   - Detectar tipos de relaciones faltantes (duplicados, dependencias)
   - Construir matriz de adyacencia entre incidencias relacionadas

3. **Focos problemáticos:**
   - Analizar por componente, temporalidad y gravedad
   - Detectar incrementos anómalos en frecuencia de incidencias
   - Calcular densidad de problemas por módulo/funcionalidad
   - Identificar componentes con alta concentración de bugs sin resolver
   - Destacar tendencias y acumulaciones críticas
   
4. **Análisis Temporal:**
   - Categorizar por fecha de creación (diaria/semanal)
   - Analizar tiempos medios de resolución por componente
   - Identificar ciclos o patrones de aparición
   - Correlacionar con eventos conocidos (releases, actualizaciones)
   
5. **Clasificación de Gravedad:**
   - Combinar prioridad oficial + impacto real observado
   - Detectar inconsistencias entre prioridad asignada y comportamiento
   - Identificar tickets con alto impacto pero baja prioridad

---

## 📊 FORMATO DE SALIDA OBLIGATORIO

### Informe Ejecutivo

```markdown
## 📊 ANÁLISIS DE INCIDENCIAS: [PRODUCTO/ENABLER]

### RESUMEN EJECUTIVO
| Categoría | Cantidad | % del Total | Tendencia (30d) | Foco Principal | Salud |
|-----------|----------|-------------|----------------|----------------|-------|
| Incidencias Totales | [Número] | 100% | [↑/↓/→] [±%] | - | [🟢/🟡/🔴] |
| Incidencias Aisladas | [Número] | [%] | [↑/↓/→] [±%] | [Componente] | [🟢/🟡/🔴] |
| Incidencias Relacionadas | [Número] | [%] | [↑/↓/→] [±%] | [Componente] | [🟢/🟡/🔴] |
| Incidencias Críticas | [Número] | [%] | [↑/↓/→] [±%] | [Componente] | [🟢/🟡/🔴] |
| Sin Asignar | [Número] | [%] | [↑/↓/→] [±%] | [Componente] | [🟢/🟡/🔴] |

### FOCOS DE PROBLEMAS IDENTIFICADOS
| Componente | Incidencias | % del Total | Relaciones Faltantes | Gravedad Media | Score de Riesgo |
|------------|-------------|-------------|----------------------|----------------|----------------|
| [Nombre] | [Número] | [%] | [Número] | [Alta/Media/Baja] | [1-10] |
| [Nombre] | [Número] | [%] | [Número] | [Alta/Media/Baja] | [1-10] |

### Clusters de Incidencias
```markdown
### 📎 CLUSTER: [NOMBRE DESCRIPTIVO]

#### Tickets Relacionados
| ID | Título | Estado | Prioridad | Componente | Relación |
|----|--------|--------|-----------|------------|----------|
| [ID1] | [Título] | [Estado] | [Prioridad] | [Componente] | - |
| [ID2] | [Título] | [Estado] | [Prioridad] | [Componente] | [Tipo Relación] |

#### Análisis de Cluster
- **Patrón común**: [Descripción del patrón detectado]
- **Root cause probable**: [Causa raíz identificada o hipótesis]
- **Impacto agregado**: [Bajo/Medio/Alto]
- **Score de cohesión**: [1-10]
```

### Incidencias Críticas Aisladas
```markdown
### 🚨 INCIDENCIA CRÍTICA AISLADA: [ID_TICKET]

#### [TÍTULO]
- **Componente**: [Componente]
- **Reportado por**: [Usuario]
- **Creado**: [Fecha]
- **Estado**: [Estado]
- **Link**: https://jira.inditex.com/jira/browse/[ID_TICKET]

#### Análisis
- **Debería relacionarse con**: [Tickets similares]
- **Justificación**: [Razones]
- **Impacto estimado**: [Bajo/Medio/Alto]
- **Score de gravedad**: [1-10]
- **Tiempo sin asignar**: [Días/Horas]


### Recomendaciones
```markdown
### 📝 RECOMENDACIONES: [COMPONENTE/ÁREA]

#### Acciones Sugeridas
1. **Consolidación**: [Específicas]
2. **Revisión prioritaria**: [Específicas]
3. **Relaciones faltantes**: [Específicas]

#### Plan de Acción
| Acción | Tickets Relacionados | Prioridad | Impacto Esperado |
|--------|----------------------|-----------|------------------|
| [Acción] | [ID1], [ID2] | [Alta/Media/Baja] | [Descripción] |
```

---

## ⚠️ CONSIDERACIONES ESPECÍFICAS PARA BUGS

### Validación Especializada
- **Campo crítico:** Verificar que `"Products/Enablers - Affected"` tenga valores válidos
- **Expandir búsqueda:** Si no hay resultados, ampliar periodo temporal gradualmente
- **Consistencia:** Validar que MCP y JSON tengan datos coherentes para cada bug

---

## � TÉCNICAS AVANZADAS DE ANÁLISIS

1. **Análisis de Tendencias**
   - Aplicar regresión lineal simple para proyectar evolución de incidencias
   - Calcular velocidad de resolución vs. creación para determinar acumulación
   - Detectar patrones cíclicos o estacionales en la aparición de bugs

2. **Clustering Semántico**
   - Vectorizar descripciones y aplicar técnicas de similitud textual
   - Agrupar por similitud de palabras clave y componentes afectados
   - Identificar terminología común en clusters para determinar causas raíz

3. **Análisis de Redes**
   - Construir grafos de relaciones entre incidencias
   - Calcular centralidad y densidad de conexiones
   - Identificar nodos críticos que conectan múltiples clusters

4. **Detección de Anomalías**
   - Identificar desviaciones significativas en métricas clave
   - Detectar componentes con comportamiento atípico (alta tasa de bugs, bajo ratio resolución)
   - Alertar sobre incidencias con patrones inusuales

---

## 🎯 REGLAS ESPECÍFICAS PARA ANÁLISIS DE BUGS

### Obligatorio en Análisis de Incidencias
- ✅ **Incluir enlaces JIRA** para cada incidencia analizada
- ✅ **Aplicar métricas de severidad** normalizadas (1-10)
- ✅ **NO ignorar incidencias aisladas** - son críticas para el análisis
- ✅ **Aportar evidencia** para cada hipótesis sobre clusters
- ✅ **Calcular scores de riesgo** usando algoritmos definidos

## 📈 ALGORITMOS DE CÁLCULO DE MÉTRICAS

### Score de Riesgo de Componente
```
RiesgoComponente = (NumIncidencias/Total * 0.3) + (PromedioSeveridad/10 * 0.3) + 
                  (IncidenciasSinResolver/NumIncidencias * 0.2) + (TiempoMedioResolución/MaxTiempo * 0.2)
```

### Score de Aislamiento
```
ScoreAislamiento = (Prioridad/MaxPrioridad * 0.4) + (DíasSinResolver/30 * 0.3) + 
                  (SimilitudConOtrosTickets * 0.3)
```

### Score de Cohesión de Cluster
```
ScoreCohesión = (RelacionesDirectas * 0.4) + (SimilitudComponentes * 0.3) + 
               (SimilitudTextual * 0.3)
```

### Indicador de Salud
- 🟢 Score < 3.5
- 🟡 Score entre 3.5 y 7
- 🔴 Score > 7
