import os
import sys
import logging
import json
import argparse
import requests
from pathlib import Path
import datetime
import hashlib
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from utils.printer import save_json_to_file
from utils.env_loader import load_env_vars

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def build_parser():
    parser = argparse.ArgumentParser(description="Execute JQL queries in Jira - Generates reports in ALL formats by default")
    parser.add_argument("-m", action="store_true", help="Show menu mode")
    parser.add_argument("jql", nargs="?", help="JQL query to execute (if not provided, DEFAULT_JQL from .env will be used)")
    parser.add_argument("-e", "--env", help="Path to .env file with credentials")
    parser.add_argument("--max-results", type=int, default=50, help="Maximum number of results to return (default: 50)")
    return parser

def extract_required_fields(issue):
    fields = issue.get('fields', {})
    return {
        "id": issue.get('key'),
        "title": fields.get('summary', ''),
        "description": fields.get('description', ''),
        "status": fields.get('status', {}).get('name', ''),
        "assignee": (fields.get('assignee', {}) or {}).get('displayName', '') if fields.get('assignee') else '',
        "reporter": (fields.get('reporter', {}) or {}).get('displayName', '') if fields.get('reporter') else '',
        "created": fields.get('created', ''),
        "duedate": fields.get('duedate', '')
    }

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.m:
        from menu.menu import main_menu
        main_menu()
        return 0

    if not load_env_vars(args.env):
        logger.error("Could not load environment variables.")
        return 1

    jql_query = args.jql or os.environ.get("DEFAULT_JQL")
    if not jql_query:
        logger.error("No JQL query provided and no DEFAULT_JQL in .env")
        return 1

    fields = ["summary", "status", "assignee", "reporter", "created", "duedate"]

    results = execute_jql(
        jql_query=jql_query,
        max_results=args.max_results,
        fields=fields
    )
    nested = []
    for issue in results:
        entry = extract_required_fields(issue)
        entry["children"] = get_children_tickets(issue.get('key'))
        nested.append(entry)

    json_nested_file = save_json_to_file(
        nested, 
        jql_query + "_nested", 
        output_dir="reports/json", 
        prefix="query_nested", 
        custom_timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    return 0 if results else 1

logger = logging.getLogger("JqlQuery")

def get_children_tickets(issue_key):
    results = execute_jql(f'"Parent Link" = {issue_key}', max_results=100)
    formatted_results = []
    for issue in results:
        formatted_results.append(extract_required_fields(issue))
    return formatted_results

def execute_jql(jql_query, max_results=50, fields=None):
    try:
        # Get credentials
        jira_server = os.environ.get("JIRA_SERVER", "").strip()
        jira_token = os.environ.get("JIRA_TOKEN", "").strip()
        if not jira_server or not jira_token:
            
            print("Missing Jira credentials in environment variables")
            return False
        if jira_server.endswith('/'):
            jira_server = jira_server[:-1]
        api_url = f"{jira_server}/rest/api/2/search"
        logger.info(f"Executing JQL query: {jql_query}")
        logger.info(f"Maximum results: {max_results}")
        
        if not fields:
            fields = ["summary", "status", "assignee", "updated", "created", "priority", "issuetype"]
        params = {
            "jql": jql_query,
            "maxResults": max_results,
            "fields": ",".join(fields)
        }
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {jira_token}"
        }
        response = requests.get(api_url, params=params, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            issues = data.get('issues', [])
            total = data.get('total', 0)
            logger.info(f"Query successful! Found {len(issues)} issues (of {total} total).")
            return issues
        else:
            logger.error(f"Error in query: {response.status_code}")
            logger.error(f"Details: {response.text[:500]}")
            return False
    except Exception as e:
        logger.error(f"Error executing JQL query: {str(e)}")
        return False
    
# Main function is defined above

if __name__ == "__main__":
    sys.exit(main())
