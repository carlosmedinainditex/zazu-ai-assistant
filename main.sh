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
    
    python3 handler/jql_query.py "$2"
else
    # Default to menu mode
    python3 menu/menu.py --shell
fi
