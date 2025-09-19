# Jira API Tools

A suite of tools for interacting with the Jira API, with support for Bearer Token authentication.

## Features

- ✅ **Complete Diagnostics**: Verifies connectivity and credentials with the Jira API
- ✅ **JQL Queries**: Executes queries in Jira Query Language format and exports in various formats
- ✅ **Issue Details**: Displays complete information about any issue
- ✅ **Security**: Uses Bearer Token authentication (more secure than username and password)
- ✅ **Multiple Report Formats**: Export results as JSON, Markdown lists, or tables
- ✅ **Color-coded Outputs**: Enhanced terminal output with color formatting
- ✅ **Modular Design**: Easily extendable architecture using utility modules

## Directory Structure

```
jiratools/
├── config/                  # Configuration files for script behavior
│   ├── colors.py            # Color configuration for Python scripts
│   └── colors.sh            # Color configuration for shell scripts
├── diagnosis/               # Scripts to diagnose the connection to Jira
│   └── diagnostic.py        # Connection diagnostics (supports both complete and simple modes)
├── env/                     # Configuration files and environment variables
│   ├── .env                 # Environment variables for scripts (not included in repo)
│   ├── .env.example         # Template for creating the .env file
│   └── README.md            # Documentation about environment variables
├── handler/                 # Handlers for Jira API queries
│   ├── jql_query.py         # Executes JQL queries and returns results in various formats
│   └── issue_query.py       # Queries details of a specific issue
├── menu/                    # Menus and user interfaces
│   └── menu.py              # Interactive menu to access functionalities
├── reports/                 # Output formats for query results
│   ├── json/                # JSON format export templates
│   └── markdown/            # Markdown format export templates
│       ├── list/            # List-style markdown output
│       └── table/           # Table-style markdown output
├── req/                     # Project requirements
│   └── requirements.txt     # Python dependencies list
├── utils/                   # Utility modules for common functions
│   ├── env_loader.py        # Environment variable loading utility
│   ├── printer.py           # Output formatting and display utilities
│   └── script_runner.py     # Script execution utilities
├── main.sh                  # Main bash script for interacting with tools
└── README.md                # This documentation file
```

## Component Descriptions

### Configuration (config/)
- **colors.py**: Defines color constants for Python scripts to enhance terminal output readability.
- **colors.sh**: Provides color definitions for shell scripts with ANSI color codes.

### Diagnostics (diagnosis/)
- **diagnostic.py**: Complete diagnostic script that tests the connection to different Jira API endpoints using Bearer Token authentication. Displays detailed information about the response and the connected user. Can be run with the `--simple` flag for a basic connection test with minimal output.

### Environment (env/)
- Contains configuration files for connecting to the Jira API.
- **README.md**: Documentation about required environment variables and how to set them up.

### Handlers (handler/)
- **jql_query.py**: Executes JQL queries (Jira Query Language) and displays results in various formats (simple, JSON, table, markdown). Supports configuration of maximum results and fields to include.
- **issue_query.py**: Retrieves detailed information about a specific Jira issue. Allows expanding specific fields and displaying results in different formats (simple, JSON, detailed).

### Menu (menu/)
- **menu.py**: Provides an interactive CLI menu to access all functionalities without needing to remember specific commands.

### Reports (reports/)
- Templates and utilities for formatting query results in different output formats:
  - **json/**: JSON format export templates and handlers
  - **markdown/**: 
    - **list/**: List-style markdown export format
    - **table/**: Table-style markdown export format

### Requirements (req/)
- **requirements.txt**: List of Python dependencies required for the project.

### Utilities (utils/)
- **env_loader.py**: Utility to load and validate environment variables from `.env` files.
- **printer.py**: Handles formatted output to the terminal with color coding and different styles.
- **script_runner.py**: Provides functions to execute shell commands and scripts from Python.

## Installation & Setup

### Requirements

- Python 3.6+
- Required libraries (listed in `req/requirements.txt`):
  - requests: HTTP communication with the Jira API
  - python-dotenv: Loading environment variables
  - texttable: Terminal table formatting
  - colorama: Terminal color formatting
  - other dependencies as listed in requirements.txt

### Installation Steps

1. Clone this repository or download the scripts:
   ```bash
   git clone https://github.com/yourusername/jiratools.git
   cd jiratools
   ```

2. Install the dependencies:
   ```bash
   pip install -r req/requirements.txt
   ```

3. Configure the environment file:
   ```bash
   cp env/.env.example env/.env
   # Edit with your preferred editor
   nano env/.env  # or vim, code, etc.
   ```

4. Make the main script executable:
   ```bash
   chmod +x main.sh
   ```

## Usage

### Environment Configuration

All scripts require a `.env` file in the `env/` folder with Jira credentials:

```
JIRA_SERVER=https://jira.example.com
JIRA_USER=your_username
JIRA_TOKEN=your_api_token
```

### Using the Interactive Menu

The easiest way to use the tools is by executing the main script:

```bash
# Execute the main script
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

# Execute a JQL query with table output (max 10 results)
python3 handler/jql_query.py "project = PROJECT ORDER BY created DESC" -m 10 -o table

# Execute a JQL query with markdown output
python3 handler/jql_query.py "project = PROJECT ORDER BY created DESC" -o markdown

# Get issue details in detailed format
python3 handler/issue_query.py PROJECT-123 -o detailed

# Get issue details in JSON format
python3 handler/issue_query.py PROJECT-123 -o json
```

## Export Options

The tools support various export formats:

- **Simple**: Basic text output in the terminal
- **JSON**: Structured JSON output (can be redirected to a file)
- **Table**: Formatted ASCII tables for terminal display
- **Markdown**: Markdown output in list or table format for documentation

Example:
```bash
# Export JQL results to a JSON file
python3 handler/jql_query.py "project = PROJECT" -o json > results.json

# Export issue details to a markdown file
python3 handler/issue_query.py PROJECT-123 -o markdown > issue.md
```

## Advanced Usage

### Custom Report Formats

You can create custom report templates in the `reports/` directory:

1. Add your template to the appropriate subfolder
2. Modify the handler scripts to include your new format

### Adding New Functionality

To add new functionality:

1. Create a new handler in the `handler/` directory
2. Update the menu in `menu/menu.py` to include your new feature
3. If needed, add any utility functions to the `utils/` directory

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

Please ensure your code follows the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
