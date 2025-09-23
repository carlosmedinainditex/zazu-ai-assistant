#!/usr/bin/env python3
"""
Main menu for Jira tools.
This script provides a simplified interface for Jira operations including connection testing,
JQL queries, and issue details retrieval.
"""

import os
import sys
import shlex
from pathlib import Path

# Get the current directory path
SCRIPT_DIR = Path(__file__).parent.parent.absolute()

# Add config directory to the Python path to import the colors module
sys.path.append(str(SCRIPT_DIR))

# Import colors directly from the colors.py module
from config.colors import RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE, BOLD, NC
# Import script runner utilities
from utils.script_runner import run_script, run_shell_command

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title="JIRA TOOLS"):
    """Prints a header for the menu with colors"""
    clear_screen()
    print(f"{BLUE}============================================={NC}")
    print(f"{BLUE}            {title}              {NC}")
    print(f"{BLUE}============================================={NC}")
    print()
    
def run_jql_query():
    """Runs a JQL query"""
    jql_query = input("Enter JQL query: ")
    
    max_results = input("Maximum results [50]: ")
    max_results = max_results if max_results else "50"
    
    # Default to table format for the shell version
    output_format = input("Output format [mdtable]: ")
    output_format = "mdtable"
    print(f"{YELLOW}Using table format for output{NC}")
    
    print(f"{BLUE}Running JQL query...{NC}")
    cmd_args = []
    if jql_query:
        # Don't use shlex.quote for JQL queries as it can interfere with syntax
        cmd_args.append(jql_query)
    
    cmd_args.extend(["--max-results", max_results, "-o", output_format])
    
    run_script(SCRIPT_DIR / "handler" / "jql_query.py", *cmd_args)
    
def query_issue():
    """Queries a specific issue"""
    print(f"{BLUE}Get issue details{NC}")
    issue_key = input("Enter issue key (e.g., PROJ-123): ")
    
    if not issue_key:
        print(f"{RED}No valid issue key provided.{NC}")
        input(f"{YELLOW}Press ENTER to continue...{NC}")
        return
    
    # Always use detailed format
    output_format = "detailed"
    print(f"{YELLOW}Using detailed format for output{NC}")
    
    print(f"{BLUE}Querying issue {issue_key}...{NC}")
    run_script(SCRIPT_DIR / "handler" / "issue_query.py", issue_key, "-o", output_format)

# Función diagnosis_menu eliminada en favor de llamar directamente al diagnóstico completo

def shell_menu():
    """Main menu for the Jira tools application"""
    while True:
        print_header("JIRA TOOLS")
        print(f"{GREEN}1. Run complete Jira connection diagnosis{NC}")
        print(f"{GREEN}2. Execute JQL query{NC}")
        print(f"{GREEN}3. Get issue details{NC}")
        print(f"{RED}0. Exit{NC}")
        print(f"{BLUE}============================================={NC}")
        
        option = input("Select an option: ")
        
        if option == "1":
            # Ejecutar diagnóstico completo directamente
            print(f"{BLUE}Running complete Jira connection diagnosis...{NC}")
            run_script(SCRIPT_DIR / "diagnosis" / "diagnostic.py")
        elif option == "2":
            run_jql_query()
        elif option == "3":
            query_issue()
        elif option == "0":
            print(f"{GREEN}Goodbye!{NC}")
            return 0
        else:
            print(f"{RED}Invalid option. Please try again.{NC}")
            import time
            time.sleep(1)

# Command-line argument handling
if __name__ == "__main__":
    sys.exit(shell_menu())
