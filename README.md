# 🚀 Zazu Jira API Connector

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Bearer Token Auth](https://img.shields.io/badge/Auth-Bearer%20Token-green.svg)](https://developer.atlassian.com/cloud/jira/platform/security/)

**Professional Jira API connector specialized in analyzing coverage and parent-child relationships between tickets with advanced reporting capabilities.**

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)  
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Advanced Usage](#-advanced-usage)
- [API Reference](#-api-reference)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## 🎯 Overview

Zazu Jira API Connector is a specialized Python tool designed for **enterprise-level Jira ticket analysis**, focusing on parent-child relationships and coverage reporting. It provides comprehensive insights into initiative-epic hierarchies with professional reporting capabilities.

### Core Capabilities

- **🔍 Initiative-Epic Analysis**: Complete coverage analysis between parent initiatives and child epics
- **📊 Nested Reporting**: Structured JSON/Markdown reports with full hierarchy visualization  
- **🔐 Secure Authentication**: Bearer Token authentication (enterprise security standard)
- **🎨 Multi-format Export**: JSON, Markdown lists, tables, and colored terminal output
- **⚡ Interactive Interface**: Professional menu system with command-line alternatives
- **🛠️ Extensible Architecture**: Modular design for easy customization and extension

## ✨ Key Features

| Feature | Description | Status |
|---------|-------------|--------|
| **Parent-Child Coverage** | Analyze relationships between initiatives and epics | ✅ |
| **Bearer Token Auth** | Secure API authentication method | ✅ |
| **Interactive Menu** | User-friendly terminal interface | ✅ |
| **Multiple Export Formats** | JSON, Markdown, Table outputs | ✅ |
| **Connection Diagnostics** | Comprehensive connectivity testing | ✅ |
| **JQL Query Support** | Full Jira Query Language support | ✅ |
| **Colored Output** | Enhanced terminal visualization | ✅ |
| **Modular Design** | Extensible architecture | ✅ |

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Valid Jira instance access
- API token with appropriate permissions

### 1-Minute Setup

```bash
# Clone and setup
git clone https://github.com/carlosmedinainditex/zazu-jira-api-connector.git
cd zazu-jira-api-connector

# Install dependencies
pip install -r req/requirements.txt

# Configure environment (see Configuration section)
cp .env.example .env  # Edit with your Jira credentials

# Run interactive menu
./main.sh
```

### Quick Analysis Example

```bash
# Direct initiative analysis
./main.sh -q "project = MYPROJ AND issuetype = Initiative"

# Connection test
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

The tool requires the following Python packages (automatically installed):

```txt
requests>=2.25.0          # HTTP communication
python-dotenv>=0.19.0     # Environment variable management
texttable>=1.6.0          # Terminal table formatting
colorama>=0.4.4           # Cross-platform colored terminal output
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

## 📖 Usage

### Interactive Menu (Recommended)

Launch the interactive interface for guided usage:

```bash
./main.sh
```

The menu provides:
- **Connection diagnostics**
- **Initiative-Epic analysis**
- **Custom JQL queries**
- **Individual issue lookup**
- **Export format options**

### Command Line Interface

#### Direct JQL Query Execution

```bash
# Basic initiative analysis
./main.sh -q "project = SALES AND issuetype = Initiative"

# Advanced query with date filtering
python3 handler/jql_query.py "project = SALES AND issuetype = Initiative AND created >= -30d" --max-results 20
```

#### Individual Issue Analysis

```bash
# Detailed issue information
python3 handler/issue_query.py PROJ-123 -o detailed

# JSON export
python3 handler/issue_query.py PROJ-123 -o json
```

#### Connection Diagnostics

```bash
# Full diagnostic report
python3 diagnosis/diagnostic.py

# Quick connectivity test
python3 diagnosis/diagnostic.py --simple
```

### Data Structure Examples

#### Initiative with Children (Parent Ticket)

```json
{
  "id": "PROJ-123",
  "project": "PROJ",
  "summary": "Customer Experience Initiative",
  "description": "Complete overhaul of customer journey...",
  "status": "In Progress",
  "assignee": "John Doe",
  "reporter": "Jane Smith",
  "created": "2023-01-15T10:30:00.000Z",
  "duedate": "2023-06-30",
  "owner": "Customer Success Team",    // ← Initiative-specific field
  "affected": "Sales & Marketing",    // ← Initiative-specific field
  "children": [
    {
      "id": "PROJ-124",
      "project": "PROJ", 
      "summary": "Mobile App Enhancement Epic",
      "status": "To Do",
      "assignee": "Mobile Team Lead"
      // Note: Children don't include owner/affected fields
    }
  ]
}
```

#### Epic (Child Ticket)

```json
{
  "id": "PROJ-124",
  "project": "PROJ",
  "summary": "Mobile App Enhancement Epic", 
  "description": "Improve mobile user experience...",
  "status": "In Progress",
  "assignee": "Ana Lopez",
  "reporter": "Carlos Ruiz", 
  "created": "2023-02-01T09:15:00.000Z",
  "duedate": "2023-04-15"
  // Note: No owner/affected fields (initiative-only)
}
```

## 🏗️ Project Structure

```
zazu-jira-api-connector/
├── 📁 config/                    # Configuration management
│   ├── colors.py                 # Python color schemes
│   └── colors.sh                 # Shell color schemes
├── 📁 diagnosis/                 # Connection diagnostics
│   └── diagnostic.py             # 🔍 Connection testing & validation
├── 📁 handler/                   # Core API handlers
│   ├── jql_query.py             # ⭐ Main JQL processor & parent-child analysis
│   └── issue_query.py           # Individual issue handler
├── 📁 menu/                     # User interface
│   └── menu.py                  # 🎯 Interactive menu system
├── 📁 reports/                  # Export templates
│   ├── json/                    # JSON format templates
│   └── markdown/                # Markdown export templates
│       ├── list/                # List-style output
│       └── table/               # Table-style output
├── 📁 req/                      # Dependencies
│   └── requirements.txt         # Python package requirements
├── 📁 utils/                    # Utility modules
│   ├── env_loader.py           # Environment variable loader
│   ├── printer.py              # Output formatting utilities
│   └── script_runner.py        # Script execution utilities
├── main.sh                      # 🚀 Main entry point
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
└── README.md                    # This documentation
```

### Module Responsibilities

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `handler/jql_query.py` | **Core Analysis** | JQL execution, parent-child analysis, coverage reports |
| `handler/issue_query.py` | **Issue Details** | Individual ticket information retrieval |
| `diagnosis/diagnostic.py` | **Connectivity** | API connection testing, credential validation |
| `menu/menu.py` | **Interface** | Interactive menu, user guidance |
| `utils/env_loader.py` | **Configuration** | Environment variable management |
| `utils/printer.py` | **Output** | Formatted terminal output, color management |

## 🎯 Advanced Usage

### Custom Report Templates

Create custom export formats by adding templates to the `reports/` directory:

```bash
# Create custom JSON template
mkdir -p reports/json/custom
echo '{"custom_format": "template"}' > reports/json/custom/my_template.json

# Create custom Markdown template  
mkdir -p reports/markdown/custom
echo "# Custom Report Template" > reports/markdown/custom/my_template.md
```

### Extending Functionality

#### Adding New Handlers

1. Create new handler in `handler/` directory:
```python
# handler/my_custom_handler.py
def custom_analysis(jql_query):
    # Your custom logic here
    pass
```

2. Update menu system:
```python
# menu/menu.py - Add new menu option
def show_custom_option():
    # Menu integration
    pass
```

3. Add utilities if needed:
```python
# utils/my_utility.py
def helper_function():
    # Utility functions
    pass
```

### Environment-Specific Configurations

#### Development Environment
```env
# .env.dev
JIRA_SERVER=https://dev-jira.company.com
MAX_RESULTS=10
DEBUG=true
```

#### Production Environment
```env
# .env.prod
JIRA_SERVER=https://jira.company.com
MAX_RESULTS=100
TIMEOUT=30
```

#### Usage with Different Environments
```bash
# Load specific environment
cp .env.dev .env
python3 diagnosis/diagnostic.py
```

### Advanced JQL Queries

#### Time-Based Analysis
```bash
# Initiatives created this quarter
python3 handler/jql_query.py "project = SALES AND issuetype = Initiative AND created >= startOfQuarter()"

# Recently updated initiatives with their epics
python3 handler/jql_query.py "project = SALES AND issuetype = Initiative AND updated >= -7d"
```

#### Status-Based Coverage
```bash
# Active initiatives and their epic status
python3 handler/jql_query.py "project = SALES AND issuetype = Initiative AND status IN ('In Progress', 'To Do')"

# Completed initiatives with unfinished epics
python3 handler/jql_query.py "project = SALES AND issuetype = Initiative AND status = Done"
```

#### Multi-Project Analysis
```bash
# Cross-project initiative analysis
python3 handler/jql_query.py "project IN (SALES, MARKETING, SUPPORT) AND issuetype = Initiative"
```

## 📚 API Reference

### Core Functions

#### `jql_query.py`

```python
def execute_jql_query(jql, max_results=50):
    """
    Execute JQL query and return results with parent-child analysis.
    
    Args:
        jql (str): Jira Query Language string
        max_results (int): Maximum number of results to return
        
    Returns:
        dict: Structured results with children hierarchy
    """
```

#### `issue_query.py`

```python
def get_issue_details(issue_key, output_format='detailed'):
    """
    Retrieve detailed information for a specific issue.
    
    Args:
        issue_key (str): Jira issue key (e.g., 'PROJ-123')
        output_format (str): Output format ('detailed', 'json', 'simple')
        
    Returns:
        dict: Issue details with all fields
    """
```

#### `diagnostic.py`

```python
def test_http_connection():
    """
    Test connection to Jira API with current credentials.
    
    Returns:
        bool: True if connection successful, False otherwise
    """
```

### Command Line Arguments

#### JQL Query Handler
```bash
python3 handler/jql_query.py [JQL_QUERY] [OPTIONS]

Options:
  --max-results NUM    Maximum number of results (default: 50)
  --output FORMAT      Output format: simple, json (default: simple)
  --file FILENAME      Save results to file
```

#### Issue Query Handler  
```bash
python3 handler/issue_query.py [ISSUE_KEY] [OPTIONS]

Options:
  -o, --output FORMAT  Output format: detailed, json, simple (default: detailed)
  --file FILENAME      Save results to file
```

#### Diagnostic Tool
```bash
python3 diagnosis/diagnostic.py [OPTIONS]

Options:
  --simple            Quick connectivity test only
  --verbose           Detailed diagnostic information
```

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
# Solution: Check proxy settings or add certificate verification skip
export PYTHONHTTPSVERIFY=0  # Temporary workaround
```

#### Query Problems

**Issue**: `No Results Returned`
```bash
# Solution: Test JQL in Jira web interface first
# Verify project permissions and field accessibility
python3 handler/jql_query.py "project = YOURPROJECT" --max-results 5
```

**Issue**: `Field Not Found Error`
```bash
# Solution: Custom fields vary between Jira instances
# Use Jira REST API to list available fields:
curl -H "Authorization: Bearer YOUR_TOKEN" \
     "https://your-jira.com/rest/api/2/field"
```

#### Permission Issues

**Issue**: `Forbidden (403)` errors
- Verify API token has appropriate permissions
- Check project access permissions
- Ensure user has read access to required issue types

### Debug Mode

Enable detailed logging for troubleshooting:

```bash
# Set debug environment variable
export DEBUG=true

# Run with verbose output
python3 diagnosis/diagnostic.py --verbose
```

### Log Files

The tool creates log files for debugging:

```bash
# View recent logs
tail -f logs/zazu-jira-connector.log

# Search for specific errors
grep -i "error" logs/zazu-jira-connector.log
```

### Performance Optimization

#### Large Dataset Handling

```bash
# For large datasets, use pagination
python3 handler/jql_query.py "your-query" --max-results 100

# Process in batches for very large projects
for i in {0..500..100}; do
    python3 handler/jql_query.py "your-query" --start-at $i --max-results 100
done
```

#### Network Optimization

```env
# Add to .env for slow networks
TIMEOUT=60
RETRY_ATTEMPTS=3
CONNECTION_POOL_SIZE=10
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Setup

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/your-username/zazu-jira-api-connector.git
cd zazu-jira-api-connector

# 3. Create development branch
git checkout -b feature/your-feature-name

# 4. Install development dependencies
pip install -r req/requirements.txt
pip install -r req/requirements-dev.txt  # If available

# 5. Make your changes and test
python3 diagnosis/diagnostic.py --simple
```

### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Documentation**: Add docstrings to all functions
- **Testing**: Include tests for new functionality
- **Logging**: Use appropriate logging levels

### Submitting Changes

```bash
# 1. Commit your changes
git add .
git commit -m "feat: add new functionality for X"

# 2. Push to your fork
git push origin feature/your-feature-name

# 3. Create Pull Request on GitHub
```

### Contribution Areas

We especially welcome contributions in:

- 🔧 **New Export Formats**: Additional report templates
- 🎯 **Enhanced Analysis**: New analytical capabilities  
- 🛠️ **Utility Functions**: Helper tools and utilities
- 📚 **Documentation**: Improved guides and examples
- 🧪 **Testing**: Unit tests and integration tests
- 🎨 **UI/UX**: Enhanced menu system and user experience

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Zazu Jira API Connector

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

<div align="center">

**Built with ❤️ for Jira analysis and reporting**

[⬆ Back to Top](#-zazu-jira-api-connector)

</div>
