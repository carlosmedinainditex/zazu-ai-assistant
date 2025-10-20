# 🚀 Zazu - AI-Powered Jira Analysis Agent

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Integration](https://img.shields.io/badge/MCP-Atlassian-blue.svg)](https://github.com/modelcontextprotocol)
[![AI Agent](https://img.shields.io/badge/AI-Agent-purple.svg)](https://github.com)

**AI-specialized agent for JIRA automation and intelligent analysis. Expert in initiative coverage, bug clustering, and project scope evaluation with MCP Atlassian integration.**

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage Modes](#-usage-modes)
- [Analysis Types](#-analysis-types)
- [Project Structure](#-project-structure)
- [MCP Integration](#-mcp-integration)
- [Data Structure Reference](#-data-structure-reference)

## 🎯 Overview

**Zazu** is an AI-powered agent specialized in **automated JIRA analysis and project intelligence**. It combines advanced script automation with MCP Atlassian integration to provide deep insights into initiatives, epics, bugs, and project coverage.

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Valid Jira instance access
- API Bearer Token with appropriate permissions
- (Optional) MCP Atlassian server configured

### 1-Minute Setup

```bash
# Clone and setup
git clone https://github.com/carlosmedinainditex/zazu-jira-api-connector.git
cd zazu-jira-api-connector

# Install dependencies
pip install -r req/requirements.txt

# Configure environment
cp .env.example .env  # Edit with your Jira credentials

# Run interactive menu
./main.sh
```

### Dependencies

```txt
requests>=2.25.0          # HTTP communication
python-dotenv>=0.19.0     # Environment variable management
texttable>=1.6.0          # Terminal table formatting
colorama>=0.4.4           # Cross-platform colored output
```

## 🌍 Configuration

### Environment Variables

Create a `.env` file in the project root directory:

```env
# === REQUIRED CONFIGURATION ===
JIRA_SERVER=https://your-company.atlassian.net
JIRA_USER=your.email@company.com
JIRA_TOKEN=your_api_token_here
```

### 🔐 Obtaining Jira API Token

1. **Navigate to Jira**: Go to your Jira profile → **Account Settings**
2. **Security Section**: Find **"Create and manage API tokens"**
3. **Create Token**: Generate a new token with a descriptive name
4. **Copy Token**: Use the generated token as `JIRA_TOKEN` in your `.env` file

> **🛡️ Security Note**: Always use API tokens instead of passwords for enhanced security.

### Configuration Validation

```bash
# Test your configuration
python3 diagnosis/diagnostic.py
```

## 📖 Usage Modes

Zazu operates in **two complementary modes**:

### 🤖 AI Agent Mode (Recommended)

Interact naturally with Zazu using conversational language. The AI agent automatically:
- Translates your request to JQL
- Executes the appropriate scripts
- Analyzes the data
- Generates executive reports

**Activation**: Simply mention "Zazu" in your request.

**Examples:**
```
"Zazu, analyze initiatives in Provider vertical"
"Zazu, show bugs from IOPPROSU project for Product Platform"
"Zazu, evaluate scopes and detect gaps"
"Zazu, what are the critical issues in Engineering?"
```

### 🔧 Script Mode (Direct Execution)

Execute JQL queries directly for raw data extraction:

```bash
# Direct JQL query
./main.sh -q "issuetype = Initiative AND status = 'In Progress'"

# Maximum results control
./main.sh -q "project = AP AND issuetype = Bug" --max-results 500
```

### 🎯 Interactive Menu Mode

Launch the menu for guided navigation:

```bash
./main.sh
```
## 🔍 Analysis Types

### 1. 📊 Initiative Scope Analysis

**Purpose**: Evaluate coverage between initiatives and their child epics, detect functional gaps.

**Activation Triggers:**
- "analyze scopes"
- "evaluate scopes"
- "what's missing"
- "gaps detection"

**Process:**
1. Validates initiative existence
2. Retrieves all child epics
3. Analyzes descriptions for scope alignment
4. Scores coverage (1-5 scale)
5. Identifies missing epics and extras

**Output Format:**
```markdown
| KEY | Initiative | Epics | Score | Gaps | Extras | Action |
|-----|------------|-------|-------|------|--------|--------|
| AP-123 | Customer Portal | 8 | 4/5 | 2 | 0 | Add Mobile & API epics |
```

**Scoring System:**
- **5/5**: Perfect alignment (90-100%)
- **4/5**: Well aligned (70-90%)
- **3/5**: Moderate alignment (50-70%)
- **2/5**: Poor alignment (30-50%)
- **1/5**: Misaligned (<30%)

**Critical Rules:**
- ✅ Only analyzes **functional** gaps (business features, technical components)
- ❌ Ignores UX, Testing, QA, Validation
- ✅ Requires epic descriptions via MCP if not in JSON
- ✅ Score = 0/5 if no child epics or no descriptions

### 2. 🐛 Bug Analysis & Clustering

**Purpose**: Identify patterns, clusters, and critical issues in bug reports.

**Activation Triggers:**
- "bugs from [Product]"
- "incidents from [Enabler]"
- "IOPPROSU bugs"
- "analyze problems"

**Process:**
1. **Product Validation**: Verifies product exists via custom fields
2. **JQL Construction**: Builds optimized query based on context
3. **Data Extraction**: Executes script and loads fresh JSON
4. **Pattern Detection**: Groups bugs by semantic similarity
5. **Clustering**: Identifies related issues and isolated cases
6. **Executive Report**: Generates actionable insights

**Output Format:**
```markdown
## 📊 BUG ANALYSIS: [PRODUCT]
### ORIGIN: ALL/IOPPROSU/NON-IOPPROSU | TOTAL: X ISSUES | X CLUSTERS

### CRITICAL CLUSTERS
| Cluster | #Bugs | Typology | Component | Primary Action |
|---------|-------|----------|-----------|----------------|
| API Timeout | 5 | Timeout | Payment API | Increase timeout config |
```

**Clustering Methodology:**
- **Semantic Similarity**: Patterns in descriptions (error types, stack traces)
- **Component/Module**: Common affected areas
- **Temporality**: Issues reported in close time windows
- **Technical Typology**: NullPointer, Timeout, Memory Leak, etc.

**Special Modes:**
- **IOPPROSU Analysis**: Removes environment filters, includes all issue types
- **Production Analysis**: Filters by `Entorno Incidencia = Produccion`
- **Adaptive Search**: Expands time window if no results (-90d → -180d → -365d)

### 3. 🎯 Natural Language Queries

The AI agent automatically translates natural language to JQL:
**Examples:**
```
"initiatives in Provider" 
→ "Vertical Owner" = "Provider" AND issuetype = initiative

"bugs from Product Platform in project IOPPROSU"
→ ("Products/Enablers - Affected" = "Product Platform") AND project = "IOPPROSU" AND issuetype = Bug

"epics in Validate Priority from Engineering"
→ "Vertical Owner" = "Engineering" AND status = "Validate Priority" AND issuetype = Épica
```

## 🏗️ Project Structure

```
zazu-ai-assistant/
├── 📁 .github/                   # AI Agent Configuration
│   ├── chatmodes/                # 🤖 AI agent behaviors
│   ├── instructions/             # 🧠 Specialized analysis rules
│   │   ├── bugs.instructions.md  # Bug analysis methodology
│   │   ├── initiatives.instructions.md  # Scope analysis rules
│   │   └── spikes.instructions.md  # Spike analysis methodology
│   └── prompts/                  # AI prompt configurations
├── 📁 config/                    # Configuration management
│   ├── colors.py                 # Python color schemes
│   └── colors.sh                 # Shell color schemes
├── 📁 diagnosis/                 # Connection diagnostics
│   └── diagnostic.py             # 🔍 API connectivity testing
├── 📁 env/                       # Environment configuration
│   ├── .env                      # 🔐 Credentials (not in repo)
│   └── .env.example              # Environment template
├── 📁 handler/                   # Core API handlers
│   ├── issue_query.py            # Individual issue retrieval
│   └── jql_query.py              # ⭐ Main JQL processor with pagination
├── 📁 menu/                      # User interface
│   └── menu.py                   # 🎯 Interactive menu system
├── 📁 reports/                   # Generated reports
│   ├── json/                     # 📊 Timestamped JSON outputs
│   └── md/                       # 📄 Markdown executive reports
├── 📁 req/                       # Dependencies
│   └── requirements.txt          # Python packages
├── 📁 scripts/                   # Additional scripts (empty)
├── 📁 utils/                     # Utility modules
│   ├── env_loader.py             # Environment variable loader
│   ├── printer.py                # Output formatting
│   └── script_runner.py          # Script execution
├── main.sh                       # 🚀 Main entry point
└── README.md                     # This documentation
```

### 📊 Custom Field Reference

Zazu uses specific custom fields for Inditex JIRA instance:

| Field Name | Custom Field ID | Usage |
|------------|----------------|-------|
| Vertical Owner | `customfield_43462` | Initiative ownership |
| Products/Enablers - Affected | `customfield_43463` | Affected products |
| Product/Enabler - Principal | `customfield_43462` | Primary product (alternatives) |
| Entorno Incidencia | `customfield_10824` | Bug environment (Produccion/Preproduccion) |
| Parent Link | Built-in field | Epic-Initiative relationship |

### 🛠️ Extending Zazu

#### Adding New Analysis Types

1. **Create instruction file** in `.github/instructions/`:
```markdown
---
applyTo: "**"
description: "New analysis type rules"
---
# Analysis Rules
...
```

2. **Update chatmode** in `.github/chatmodes/Zazu.chatmode.md`:
```markdown
### New Analysis Type
- **Triggers**: "analyze [new-type]"
- **JQL Pattern**: ...
```

3. **Test with AI agent**:
```
"Zazu, [trigger phrase for new analysis]"
```


```bash
# Token permissions verification
python3 diagnosis/diagnostic.py --verbose
```

## MCP Integration

Zazu leverages **Model Context Protocol (MCP) Atlassian** for enhanced JIRA data access.

### Configuration

MCP Atlassian should be configured in your AI assistant settings:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "mcp-server-atlassian",
      "args": [],
      "env": {
        "JIRA_URL": "https://your-instance.atlassian.net",
        "JIRA_USER_EMAIL": "your.email@company.com",
        "JIRA_API_TOKEN": "your-api-token"
      }
    }
  }
}
```
## 📊 Data Structure Reference

### Initiative with Children (Parent Ticket)

```json
{
  "id": "AP-12345",
  "project": "AP",
  "summary": "Customer Portal Modernization Initiative",
  "description": "Complete redesign of customer-facing portal with mobile-first approach...",
  "status": "In Progress",
  "assignee": "John Doe",
  "reporter": "Jane Smith",
  "created": "2025-01-15T10:30:00.000Z",
  "duedate": "2025-06-30",
  "owner": "Provider",              // ← Initiative-specific (customfield_43462)
  "affected": "Finished Product",   // ← Initiative-specific (customfield_43463)
  "children": [
    {
      "id": "AP-12346",
      "project": "AP",
      "summary": "Mobile App Epic",
      "description": "Native mobile application development...",
      "status": "To Do",
      "assignee": "Mobile Team Lead",
      "reporter": "John Doe",
      "created": "2025-01-20T09:00:00.000Z",
      "duedate": "2025-04-15"
      // Note: Children (epics) don't include owner/affected fields
    },
    {
      "id": "AP-12347",
      "project": "AP",
      "summary": "API Integration Epic",
      "status": "In Progress"
      // ... more child epics
    }
  ]
}
```
<div align="center">

**🤖 Built with Love By Carlos Medina and contributed by Javier Saiz and Javier Fradejas**

[⬆ Back to Top](#-zazu---ai-powered-jira-analysis-agent)

</div>
