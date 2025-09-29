# Zazu Jira API Connector

Tools for interacting with the Jira API, with support for Bearer Token authentication.

## Features

- ✅ **Complete Diagnostics**: Verifies connectivity and credentials with the Jira API
- ✅ **JQL Queries**: Executes queries in Jira Query Language format and exports in various formats
- ✅ **Issue Details**: Shows complete information about any issue
- ✅ **Security**: Uses Bearer Token authentication (more secure than username and password)
- ✅ **Multiple Report Formats**: Exports results as JSON, Markdown lists, or tables
- ✅ **Colored Output**: Enhanced terminal output with color formatting
- ✅ **Modular Design**: Easily extensible architecture using utility modules

## Project Structure

```
zazu-jira-api-connector/
├── config/                  # Configuration files for script behavior
│   ├── colors.py           # Color configuration for Python scripts
│   └── colors.sh           # Color configuration for shell scripts
├── diagnosis/               # Scripts for diagnosing Jira connection
│   └── diagnostic.py       # Connection diagnostics (supports full and simple modes)
├── handler/                 # Handlers for Jira API queries
│   ├── jql_query.py        # Executes JQL queries and returns results in various formats
│   └── issue_query.py      # Queries details of a specific issue
├── menu/                    # Menus and user interfaces
│   └── menu.py             # Interactive menu for accessing functionalities
├── reports/                 # Output formats for query results
│   ├── json/               # JSON format export templates
│   └── markdown/           # Markdown format export templates
│       ├── list/           # Markdown list-style output
│       └── table/          # Markdown table-style output
├── req/                     # Project requirements
│   └── requirements.txt    # Python dependencies list
├── utils/                   # Utility modules for common functions
│   ├── env_loader.py       # Utility for loading environment variables
│   ├── printer.py          # Output formatting and display utilities
│   └── script_runner.py    # Script execution utilities
├── main.sh                  # Main bash script for interacting with tools
├── .gitignore              # Files and directories ignored by Git
└── README.md               # This documentation file
```

## Component Description

### Configuration (config/)
- **colors.py**: Defines color constants for Python scripts to improve terminal output readability.
- **colors.sh**: Provides color definitions for shell scripts with ANSI color codes.

### Diagnostics (diagnosis/)
- **diagnostic.py**: Complete diagnostic script that tests connection to different Jira API endpoints using Bearer Token authentication. Shows detailed information about response and connected user. Can be run with `--simple` flag for basic connection test with minimal output.

### Handlers (handler/)
- **jql_query.py**: Executes JQL (Jira Query Language) queries and displays results in various formats (simple, JSON, table, markdown). Supports configuration of maximum results and fields to include.
- **issue_query.py**: Retrieves detailed information about a specific Jira issue. Allows expanding specific fields and showing results in different formats (simple, JSON, detailed).

### Menu (menu/)
- **menu.py**: Provides an interactive CLI menu to access all functionalities without needing to remember specific commands.

### Reports (reports/)
- Templates and utilities for formatting query results in different output formats:
  - **json/**: JSON format export templates and handlers
  - **markdown/**:
    - **list/**: Markdown list-style export format
    - **table/**: Markdown table-style export format

### Requirements (req/)
- **requirements.txt**: List of Python dependencies required for the project.

### Utilities (utils/)
- **env_loader.py**: Utility for loading and validating environment variables from `.env` files.
- **printer.py**: Handles formatted terminal output with color codes and different styles.
- **script_runner.py**: Provides functions for executing shell commands and scripts from Python.

## Installation and Setup

### Requirements

- Python 3.6+
- Required libraries (listed in `req/requirements.txt`):
  - requests: HTTP communication with Jira API
  - python-dotenv: Environment variable loading
  - texttable: Terminal table formatting
  - colorama: Terminal color formatting
  - other dependencies as listed in requirements.txt

### Installation Steps

1. Clone this repository or download the scripts:
   ```bash
   git clone <repository-url>
   cd zazu-jira-api-connector
   ```

2. Install dependencies:
   ```bash
   pip install -r req/requirements.txt
   ```

3. Configure environment variables:
   ```bash
   # Create a .env file in the project root directory
   touch .env
   # Edit with your preferred editor
   nano .env  # or vim, code, etc.
   ```

4. Make the main script executable:
   ```bash
   chmod +x main.sh
   ```

## Usage

### Environment Configuration

All scripts require environment variables with Jira credentials. Create a `.env` file in the root directory with:

```
JIRA_SERVER=https://jira.example.com
JIRA_USER=your_username
JIRA_TOKEN=your_api_token
```

### Using the Interactive Menu

The easiest way to use the tools is by running the main script:

```bash
# Run the main script
./main.sh
```

This will display an interactive menu with all available options.

### Direct Script Execution

You can also run individual scripts directly:

```bash
# Connection diagnostics
python3 diagnosis/diagnostic.py

# Simple connection test
python3 diagnosis/diagnostic.py --simple

# Run JQL query with table output (maximum 10 results)
python3 handler/jql_query.py "project = PROJECT ORDER BY created DESC" -m 10 -o table

# Run JQL query with markdown output
python3 handler/jql_query.py "project = PROJECT ORDER BY created DESC" -o markdown

# Get issue details in detailed format
python3 handler/issue_query.py PROJECT-123 -o detailed

# Get issue details in JSON format
python3 handler/issue_query.py PROJECT-123 -o json
```

## Export Options

The tools support various export formats:

- **Simple**: Basic text output in terminal
- **JSON**: Structured JSON output (can be redirected to file)
- **Table**: ASCII formatted tables for terminal visualization
- **Markdown**: Markdown output in list or table format for documentation

Example:
```bash
# Export JQL results to JSON file
python3 handler/jql_query.py "project = PROJECT" -o json > results.json

# Export issue details to markdown file
python3 handler/issue_query.py PROJECT-123 -o markdown > issue.md
```

## Advanced Usage

### Custom Report Formats

You can create custom report templates in the `reports/` directory:

1. Add your template to the appropriate subfolder
2. Modify handler scripts to include your new format

### Adding New Functionality

To add new functionality:

1. Create a new handler in the `handler/` directory
2. Update the menu in `menu/menu.py` to include your new feature
3. If necessary, add utility functions to the `utils/` directory

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

Please ensure your code follows the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
