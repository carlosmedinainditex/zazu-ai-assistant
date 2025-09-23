#!/bin/bash
# Script to test Jira API connection and queries

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
# Current directory
cd "$SCRIPT_DIR"

# Simple argument check for query mode
if [ "$1" = "-q" ] && [ -n "$2" ]; then
    echo -e "Executing direct JQL Query: $2"
    pip3 install -r req/requirements.txt -q
    
    # Check if we want table output
    if [ "$3" = "-t" ]; then
        output_format="mdtable"
    else
        output_format="json-nested"
    fi
    
    python3 handler/jql_query.py "$2" --max-results 50 -o "$output_format"
else
    # Default to menu mode
    python3 menu/menu.py --shell
fi
