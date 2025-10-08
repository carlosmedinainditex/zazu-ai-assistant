# 🚀 Zazu - AI-Powered Jira Analysis Agent

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Integration](https://img.shields.io/badge/MCP-Atlassian-blue.svg)](https://github.com/modelcontextprotocol)
[![AI Agent](https://img.shields.io/badge/AI-Agent-purple.svg)](https://github.com)

**AI-specialized agent for JIRA automation and intelligent analysis. Expert in initiative coverage, bug clustering, and project scope evaluation with MCP Atlassian integration.**

## 📋 Table of Contents

- [Overview](#-overview)
- [AI Agent Capabilities](#-ai-agent-capabilities)  
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Modes](#-usage-modes)
- [Analysis Types](#-analysis-types)
- [Project Structure](#-project-structure)
- [Advanced Usage](#-advanced-usage)
- [MCP Integration](#-mcp-integration)
- [Troubleshooting](#-troubleshooting)

## 🎯 Overview

**Zazu** is an AI-powered agent specialized in **automated JIRA analysis and project intelligence**. It combines advanced script automation with MCP Atlassian integration to provide deep insights into initiatives, epics, bugs, and project coverage.

### 🤖 AI Agent Features

- **🧠 Natural Language Processing**: Automatically translates user requests to JQL queries
- **🔍 Intelligent Analysis**: Scope evaluation, bug clustering, and gap detection
- **📊 Automated Reporting**: Executive summaries with actionable recommendations
- **🎯 Context-Aware**: Understands product verticals, issue types, and JIRA structures
- **⚡ Zero-Confirmation**: Acts directly without asking for permissions
- **� MCP Atlassian Integration**: Enriched data access through Model Context Protocol

## ✨ Key Capabilities

| Capability | Description | AI-Powered |
|------------|-------------|------------|
| **Scope Analysis** | Evaluate initiative-epic coverage with automatic scoring (1-5) | ✅ |
| **Bug Clustering** | Identify patterns and relationships in technical issues | ✅ |
| **Gap Detection** | Discover missing epics and functional gaps | ✅ |
| **Natural Language Queries** | "initiatives in Provider" → JQL generation | ✅ |
| **Temporal Analysis** | Bug evolution and trend identification | ✅ |
| **MCP Integration** | Real-time JIRA data enrichment | ✅ |
| **Automatic Validation** | Product, field, and status verification | ✅ |
| **Executive Reporting** | Actionable insights in table format | ✅ |

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

### AI Agent Quick Examples

```bash
# 🧠 Natural Language Analysis (AI Agent Mode)
# Just mention "Zazu" and describe what you want:

# Initiative scope analysis
"Zazu, analyze scopes of initiatives in Provider"

# Bug analysis with clustering
"Zazu, analyze bugs from Product Platform"

# Gap detection
"Zazu, what's missing in initiative AP-12345?"

# 🔧 Direct JQL Execution (Script Mode)
./main.sh -q "project = AP AND issuetype = Initiative"

# 🩺 Connection test
python3 diagnosis/diagnostic.py --simple
```

## 🔧 Installation

### Method 1: Standard Installation

```bash
# 1. Clone repository
git clone https://github.com/carlosmedinainditex/zazu-jira-api-connector.git
cd zazu-jira-api-connector

# 2. Install Python dependencies
pip install -r req/requirements.txt

# 3. Make executable
chmod +x main.sh

# 4. Verify installation
python3 diagnosis/diagnostic.py --simple
```

### Method 2: Virtual Environment (Recommended)

```bash
# 1. Create virtual environment
python3 -m venv zazu-env
source zazu-env/bin/activate  # On Windows: zazu-env\Scripts\activate

# 2. Clone and install
git clone https://github.com/carlosmedinainditex/zazu-jira-api-connector.git
cd zazu-jira-api-connector
pip install -r req/requirements.txt

# 3. Ready to use
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

# === OPTIONAL CONFIGURATION ===
DEFAULT_JQL=project = MYPROJ AND issuetype = Initiative ORDER BY created DESC
MAX_RESULTS=50

# === PROXY CONFIGURATION (if needed) ===
HTTP_PROXY=http://proxy.company.com:8080
HTTPS_PROXY=https://proxy.company.com:8080
NO_PROXY=localhost,127.0.0.1,.company.com
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

# Simple connectivity test
python3 diagnosis/diagnostic.py --simple
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

# Analysis with specific fields
python3 handler/jql_query.py "your-jql-query" --max-results 100
```

### 🎯 Interactive Menu Mode

Launch the menu for guided navigation:

```bash
./main.sh
```

Options:
- Connection diagnostics
- Initiative-Epic analysis
- Custom JQL queries
- Individual issue lookup
- Export format selection

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

**Type Mapping:**
- "initiatives" → `issuetype = initiative`
- "epics" → `issuetype = Épica`
- "stories" → `issuetype = Historia`
- "bugs" → `issuetype = Bug`
- "tasks" → `issuetype = Tarea`

**Field Interpretation:**
- **"in [value]"** → `"Vertical Owner" = "[value]"` (99% default)
- **"project [name]"** → `project = "[name]"` (only when "project" explicitly mentioned)
- **Products/Enablers** → `"Products/Enablers - Affected" = "[value]"`

**State Mapping** (via MCP validation):
- "discovery" → `status = 'Discovering'`
- "in progress" → `status = 'In Progress'`
- "done" → `status = 'Done'`

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
zazu-jira-api-connector/
├── 📁 .github/                   # AI Agent Configuration
│   ├── instructions/             # 🧠 Specialized analysis rules
│   │   ├── bugs.instructions.md  # Bug analysis methodology
│   │   └── initiatives.instructions.md  # Scope analysis rules
│   └── chatmodes/                # 🤖 AI agent behaviors
│       └── Zazu.chatmode.md      # Main agent configuration
├── 📁 config/                    # Configuration management
│   ├── colors.py                 # Python color schemes
│   └── colors.sh                 # Shell color schemes
├── 📁 diagnosis/                 # Connection diagnostics
│   └── diagnostic.py             # 🔍 API connectivity testing
├── 📁 handler/                   # Core API handlers
│   ├── jql_query.py             # ⭐ Main JQL processor with pagination
│   └── issue_query.py           # Individual issue retrieval
├── 📁 menu/                     # User interface
│   └── menu.py                  # 🎯 Interactive menu system
├── 📁 reports/                  # Generated reports
│   └── json/                    # 📊 Timestamped JSON outputs
│       └── query_nested_YYYYMMDD_HHMMSS.json
├── 📁 req/                      # Dependencies
│   └── requirements.txt         # Python packages
├── 📁 utils/                    # Utility modules
│   ├── env_loader.py           # Environment variable loader
│   ├── printer.py              # Output formatting
│   └── script_runner.py        # Script execution
├── main.sh                      # 🚀 Main entry point
├── .env                         # 🔐 Credentials (not in repo)
├── .env.example                 # Environment template
└── README.md                    # This documentation
```

### 🎯 Module Responsibilities

| Module | Purpose | AI Integration |
|--------|---------|----------------|
| `.github/instructions/bugs.instructions.md` | **Bug Analysis Rules** | Defines clustering logic, pattern detection, IOPPROSU handling |
| `.github/instructions/initiatives.instructions.md` | **Scope Analysis Rules** | Scoring methodology, gap detection, field mappings |
| `.github/chatmodes/Zazu.chatmode.md` | **AI Agent Behavior** | Natural language processing, auto-activation triggers |
| `handler/jql_query.py` | **Data Extraction** | Pagination (up to 1000 results), parent-child nesting, JSON generation |
| `diagnosis/diagnostic.py` | **Connectivity** | Bearer token validation, API endpoint testing |
| `utils/printer.py` | **Output** | Formatted reports, executive tables |
| `main.sh` | **Orchestration** | Direct query mode (`-q` flag) or menu navigation |

### 📊 Data Flow

```
User Request → AI Agent (NLP) → JQL Translation → main.sh -q "[JQL]"
                                                          ↓
                                              handler/jql_query.py
                                                          ↓
                                          Pagination Loop (1000 results)
                                                          ↓
                                              Parent-Child Nesting
                                                          ↓
                                   reports/json/query_nested_[timestamp].json
                                                          ↓
                                              AI Agent Analysis
                                                          ↓
                                          Executive Report (Tables/Insights)
```

## 🎯 Advanced Usage

### 🔄 Data Freshness Rules

**CRITICAL**: Zazu AI agent follows strict data freshness policies:

- ✅ **Always use most recent JSON** by timestamp from `/reports/json/`
- ❌ **Never use files older than 2 hours**
- ✅ **Auto-regenerate** if data is stale
- ✅ **One source of truth** per analysis session

```bash
# Check latest generated data
ls -lt reports/json/ | head -5

# Manually regenerate if needed
./main.sh -q "your-jql-query"
```

### 🎨 Custom JQL Patterns

#### Initiative Analysis Patterns

```bash
# All initiatives in specific vertical
./main.sh -q "\"Vertical Owner\" = \"Provider\" AND issuetype = initiative"

# Initiatives with affected products
./main.sh -q "\"Products/Enablers - Affected\" = \"Product Platform\" AND issuetype = initiative"

# Time-filtered initiatives
./main.sh -q "issuetype = initiative AND created >= -90d"

# Status-specific initiatives
./main.sh -q "issuetype = initiative AND status IN ('In Progress', 'Discovering')"
```

#### Bug Analysis Patterns

```bash
# Production bugs for specific product
./main.sh -q "\"Products/Enablers - Affected\" = \"Product Platform\" AND issuetype = Bug AND \"Entorno Incidencia\" = \"Produccion\""

# IOPPROSU bugs (all environments)
./main.sh -q "project = \"IOPPROSU\" AND (\"Products/Enablers - Affected\" = \"Your Product\" OR \"Product/Enabler - Principal\" = \"Your Product\")"

# Critical bugs from last 30 days
./main.sh -q "issuetype = Bug AND priority = Highest AND created >= -30d"
```

#### Cross-Vertical Queries

```bash
# Multi-vertical initiatives
./main.sh -q "\"Vertical Owner\" IN (\"Provider\", \"Finished Product\", \"Engineering\") AND issuetype = initiative"

# Parent-child relationships
./main.sh -q "\"Parent Link\" = AP-12345"
```

### 🧪 Advanced Analysis Scenarios

#### Scenario 1: Complete Initiative Health Check

```bash
# Step 1: Extract all initiatives
./main.sh -q "\"Vertical Owner\" = \"Provider\" AND issuetype = initiative"

# Step 2: Use AI agent for scope analysis
"Zazu, analyze scopes and detect gaps in Provider initiatives"

# Step 3: Review executive report with scoring
```

#### Scenario 2: Bug Pattern Investigation

```bash
# Step 1: Extract recent bugs
./main.sh -q "\"Products/Enablers - Affected\" = \"Product Platform\" AND issuetype = Bug AND created >= -90d"

# Step 2: Request clustering analysis
"Zazu, analyze bugs from Product Platform and identify clusters"

# Step 3: Review critical clusters and isolated issues
```

#### Scenario 3: Multi-Product Analysis

```bash
# Extract data for multiple products
./main.sh -q "\"Products/Enablers - Affected\" IN (\"Product A\", \"Product B\", \"Product C\") AND issuetype = Bug"

# AI-powered comparative analysis
"Zazu, compare bug patterns across Product A, B, and C"
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

### 🔧 Pagination & Performance

The `jql_query.py` handler implements automatic pagination:

```python
# Configuration in jql_query.py
--max-results 1000  # Default: retrieves up to 1000 issues
--max-results -1    # Unlimited (use with caution)
--max-results 100   # Conservative limit for testing
```

**Performance Tips:**
- Use specific filters to reduce result sets
- JIRA API limits: 100 results per page (automatically handled)
- Large datasets (>500 issues): Expect 30-60 seconds processing
- Parent-child nesting adds ~2s per 100 initiatives

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

#### Custom Report Formats

Create templates in `reports/` directory:

```bash
# Custom JSON processor
mkdir -p reports/processors
cat > reports/processors/custom_report.py << 'EOF'
def generate_custom_report(data):
    # Your custom logic
    pass
EOF
```

### 🔐 Security Best Practices

```env
# .env security checklist
✅ Never commit .env to repository
✅ Use Bearer tokens, not passwords
✅ Rotate tokens every 90 days
✅ Grant minimum required permissions
✅ Use separate tokens for dev/prod
```

```bash
# Token permissions verification
python3 diagnosis/diagnostic.py --verbose
```

## � MCP Integration

Zazu leverages **Model Context Protocol (MCP) Atlassian** for enhanced JIRA data access.

### Available MCP Tools

| Tool | Purpose | Usage |
|------|---------|-------|
| `mcp_atlassian_jira_search` | Execute JQL queries | Field validation, data enrichment |
| `mcp_atlassian_jira_get_issue` | Retrieve issue details | Description fetching for scope analysis |
| `mcp_atlassian_jira_search_fields` | Search field definitions | Status mapping, field validation |
| `mcp_atlassian_jira_batch_get_changelogs` | Changelog history | Temporal analysis, trend detection |
| `linkedIssues([ID])` | Issue relationships | Bug clustering, dependency mapping |

### When MCP is Used

**Automatic MCP Activation:**
- ✅ **Field Validation**: Verifying custom field IDs and values
- ✅ **Status Mapping**: Translating natural language states to JIRA statuses
- ✅ **Description Enrichment**: Fetching full descriptions when not in JSON
- ✅ **Product Validation**: Confirming product/enabler existence
- ✅ **Relationship Analysis**: Exploring linked issues for clustering

**Example MCP Flow:**
```
User: "Zazu, analyze bugs from Product Platform"
  ↓
AI: Validate "Product Platform" exists
  → MCP: jira_search_fields keyword="Product Platform"
  ↓
AI: Build JQL with validated field
  → JQL: "Products/Enablers - Affected" = "Product Platform" AND issuetype = Bug
  ↓
AI: Execute script
  → ./main.sh -q "[JQL]"
  ↓
AI: Enrich with descriptions if needed
  → MCP: jira_get_issue for each issue without description
  ↓
AI: Analyze and report
```

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

### MCP vs Direct API

| Aspect | MCP Tools | Direct API (Scripts) |
|--------|-----------|---------------------|
| **Speed** | Slower (real-time) | Faster (bulk extraction) |
| **Use Case** | Validation, enrichment | Mass data extraction |
| **Data Volume** | Small queries (<50 issues) | Large datasets (>1000 issues) |
| **Zazu Strategy** | Validation first, then bulk script | ✅ Optimal approach |

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Connection Problems

**Issue**: `Connection Error` or `Authentication Failed`
```bash
# Solution: Verify configuration
python3 diagnosis/diagnostic.py

# Check environment variables
cat .env | grep -E "JIRA_(SERVER|USER|TOKEN)"
```

**Issue**: `SSL Certificate Verification Failed`
```bash
# Solution: Update requests library
pip install --upgrade requests certifi

# Temporary workaround (not recommended for production)
export PYTHONHTTPSVERIFY=0
```

#### Query Problems

**Issue**: `No Results Returned`
```bash
# Solution 1: Test JQL in Jira web interface first
# Solution 2: Verify custom field IDs
python3 -c "import os; from utils.env_loader import load_env_vars; load_env_vars(); print('Server:', os.environ.get('JIRA_SERVER'))"

# Solution 3: Check permissions
./main.sh -q "issuetype = Initiative" --max-results 5
```

**Issue**: `Field Not Found Error`
- Custom fields vary between JIRA instances
- Verify field IDs in your JIRA instance:
  - Navigate to JIRA → Settings → Issues → Custom Fields
  - Note the `customfield_XXXXX` IDs
  - Update references in `handler/jql_query.py`

#### AI Agent Issues

**Issue**: AI agent not activating
- ✅ Ensure you mention "Zazu" in your request
- ✅ Use recognized trigger phrases: "analyze", "bugs from", "initiatives in"
- ✅ Check `.github/chatmodes/Zazu.chatmode.md` is loaded

**Issue**: Stale data being used
```bash
# Force fresh data generation
rm reports/json/query_nested_*.json
./main.sh -q "your-query"
```

**Issue**: Scope analysis returns 0/5 scores
- ❌ **Cause**: Epics have no descriptions
- ✅ **Solution**: Add descriptions to epics or use MCP to fetch them
- ✅ **Verification**: Check `description` field in JSON output

#### IOPPROSU-Specific Issues

**Issue**: IOPPROSU bugs not found
```bash
# Correct JQL for IOPPROSU
./main.sh -q "project = \"IOPPROSU\" AND (\"Products/Enablers - Affected\" = \"Your Product\")"

# Note: Remove environment filters for IOPPROSU
# ❌ WRONG: ... AND \"Entorno Incidencia\" = \"Produccion\"
# ✅ RIGHT: ... (no environment filter)
```

### Debug Mode

Enable detailed logging:

```bash
# Set debug environment
export DEBUG=true

# Run with verbose output
python3 diagnosis/diagnostic.py --verbose

# Check logs
tail -f logs/zazu-jira-connector.log 2>/dev/null || echo "No log file yet"
```

### Performance Optimization

#### Large Dataset Handling

```bash
# For datasets >1000 issues, use batching
for offset in 0 500 1000 1500; do
    ./main.sh -q "your-query AND created >= -90d" --max-results 500
    sleep 2  # Rate limiting
done
```

#### Network Issues

```env
# Add to .env for slow/unstable networks
TIMEOUT=120
RETRY_ATTEMPTS=5
```

### Known Limitations

| Limitation | Workaround |
|------------|------------|
| Max 1000 results per query | Split queries by date ranges or projects |
| Custom fields vary by instance | Update field IDs in `jql_query.py` |
| MCP timeout on large issue descriptions | Use direct API for bulk extraction |
| Pagination delay on >500 issues | Expected behavior, ~2s per 100 issues |

### Getting Help

1. **Check diagnostic output:**
   ```bash
   python3 diagnosis/diagnostic.py --verbose
   ```

2. **Verify JQL in JIRA UI** before using with Zazu

3. **Review instruction files** in `.github/instructions/` for analysis rules

4. **Check data freshness:**
   ```bash
   ls -lht reports/json/ | head -3
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

### Bug/Issue (Standalone)

```json
{
  "id": "IOPPROSU-9876",
  "project": "IOPPROSU",
  "summary": "NullPointerException in Payment Service",
  "description": "Stack trace: java.lang.NullPointerException at PaymentController.process()...",
  "status": "Open",
  "assignee": "Ana Lopez",
  "reporter": "System Monitor",
  "created": "2025-10-01T14:22:00.000Z",
  "duedate": null
  // Note: Bugs don't have owner/affected/children unless they're special types
}
```

### Generated Report JSON Structure

Located in `reports/json/query_nested_[timestamp].json`:

```json
[
  {
    "id": "AP-100",
    "project": "AP",
    "summary": "Initiative Title",
    "description": "Full description...",
    "status": "In Progress",
    "assignee": "Owner Name",
    "reporter": "Reporter Name",
    "created": "2025-01-01T00:00:00.000Z",
    "duedate": "2025-12-31",
    "owner": "Vertical Owner Value",
    "affected": "Affected Product Value",
    "children": [ /* array of child epics */ ]
  }
  // ... more initiatives
]
```

## 🎓 Best Practices

### For Initiative Analysis

✅ **DO:**
- Keep initiative descriptions detailed and structured
- Add descriptions to ALL child epics (required for scoring)
- Use consistent vertical owner values
- Link epics properly with Parent Link field

❌ **DON'T:**
- Leave epic descriptions empty (results in 0/5 score)
- Create initiatives without epics
- Mix different products in same initiative without clear mapping

### For Bug Analysis

✅ **DO:**
- Use consistent product/enabler values in custom fields
- Add detailed descriptions with stack traces
- Set environment correctly (Produccion/Preproduccion)
- Link related bugs explicitly

❌ **DON'T:**
- Create isolated bugs without proper categorization
- Omit component/module information
- Skip environment field for production bugs
- Leave bugs without assignee indefinitely

### For AI Agent Interaction

✅ **DO:**
- Use natural language: "Zazu, analyze initiatives in Provider"
- Be specific about products/verticals
- Request fresh data if analysis seems outdated
- Review generated JQL for accuracy

❌ **DON'T:**
- Mix multiple analysis types in one request
- Use stale data (>2 hours old)
- Skip product validation step
- Ignore 0/5 scores (indicates missing data)

## 🚦 Health Indicators

### Initiative Health Scoring

| Score | Status | Meaning | Action Required |
|-------|--------|---------|-----------------|
| 5/5 | 🟢 Excellent | 90-100% coverage | Monitor only |
| 4/5 | 🟢 Good | 70-90% coverage | Minor adjustments |
| 3/5 | 🟡 Fair | 50-70% coverage | Review gaps |
| 2/5 | 🟠 Poor | 30-50% coverage | Immediate attention |
| 1/5 | 🔴 Critical | <30% coverage | Urgent action |
| 0/5 | ⚫ Invalid | No epics/descriptions | Fix data quality |

### Bug Cluster Health

| Indicator | Healthy | Attention | Critical |
|-----------|---------|-----------|----------|
| **Isolated Bugs** | <10% | 10-25% | >25% |
| **Cluster Size** | <3 bugs | 3-7 bugs | >7 bugs |
| **Resolution Time** | <7 days | 7-30 days | >30 days |
| **Priority** | Low-Medium | High | Highest |

## 📚 Additional Resources

### JIRA Query Language (JQL)

- [Official JQL Documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- [JQL Functions Reference](https://support.atlassian.com/jira-software-cloud/docs/jql-functions/)
- [JQL Keywords](https://support.atlassian.com/jira-software-cloud/docs/jql-keywords/)

### Model Context Protocol

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Atlassian Server](https://github.com/modelcontextprotocol/servers)

### Internal Documentation

- `.github/instructions/bugs.instructions.md` - Bug analysis methodology
- `.github/instructions/initiatives.instructions.md` - Scope analysis rules
- `.github/chatmodes/Zazu.chatmode.md` - AI agent configuration

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/your-username/zazu-jira-api-connector.git
cd zazu-jira-api-connector

# Create feature branch
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r req/requirements.txt

# Make changes and test
python3 diagnosis/diagnostic.py --simple
./main.sh -q "test-query"
```

### Contribution Areas

| Area | Priority | Examples |
|------|----------|----------|
| 🧠 **AI Instructions** | High | New analysis types, improved patterns |
| 📊 **Report Formats** | Medium | CSV export, HTML dashboards |
| � **Script Optimization** | Medium | Faster pagination, caching |
| 📚 **Documentation** | High | Use cases, tutorials, examples |
| 🧪 **Testing** | High | Unit tests, integration tests |
| 🎨 **UI/UX** | Low | Enhanced menu, color schemes |

### Code Standards

- **Python**: Follow PEP 8
- **Documentation**: Add docstrings to functions
- **Comments**: Explain complex logic
- **Commit Messages**: Use conventional commits format

```bash
# Commit message format
feat: add new bug clustering algorithm
fix: correct pagination limit handling
docs: update README with MCP examples
refactor: simplify JQL query builder
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

```
Copyright (c) 2025 Zazu JIRA Analysis Agent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

**🤖 Built with AI for intelligent JIRA analysis**

**Powered by MCP Atlassian Integration**

[⬆ Back to Top](#-zazu---ai-powered-jira-analysis-agent)

</div>
