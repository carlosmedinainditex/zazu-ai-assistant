#!/usr/bin/env python3
"""
Script to query details of a specific Jira issue using Bearer token.
"""

import os
import sys
import logging
import json
import argparse
from pathlib import Path
import requests

# Add the project root to the Python path
script_dir = Path(__file__).parent.parent.absolute()
sys.path.append(str(script_dir))

# Import from utils
from utils.env_loader import load_env_vars

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("JiraIssue")

def get_issue(issue_key):
    """
    Gets information about a specific Jira issue.
    
    Args:
        issue_key (str): Key of the issue to get (eg: PROJ-123)
        
    Returns:
        dict: Issue information, or None if there's an error
    """
    try:
        # Get credentials
        jira_server = os.environ.get("JIRA_SERVER", "").strip()
        jira_token = os.environ.get("JIRA_TOKEN", "").strip()
        
        # Check if we have credentials
        if not jira_server or not jira_token:
            logger.error("Missing Jira credentials in environment variables")
            return None
        
        # Make sure URL doesn't end with /
        if jira_server.endswith('/'):
            jira_server = jira_server[:-1]
        
        # URL for issue API
        api_url = f"{jira_server}/rest/api/2/issue/{issue_key}"
        
        logger.info(f"Getting issue information: {issue_key}")
        
        # Query parameters
        params = {}
        
        # Headers with Bearer token
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {jira_token}"
        }
        
        # Make the request
        response = requests.get(api_url, params=params, headers=headers, timeout=15)
        
        # Check response
        if response.status_code == 200:
            issue_data = response.json()
            logger.info(f"Issue retrieved successfully: {issue_key}")
            return issue_data
        else:
            logger.error(f"Error getting issue: {response.status_code}")
            logger.error(f"Details: {response.text[:500]}")
            return None
        
    except Exception as e:
        logger.error(f"Error getting issue: {str(e)}")
        return None

def show_issue(issue_data, output_format="simple"):
    """
    Shows issue information according to the specified format.
    
    Args:
        issue_data (dict): Issue data
        output_format (str): Output format ('simple', 'json', 'detailed')
    """
    if not issue_data:
        logger.error("No issue data to display")
        return
    
    if output_format == "json":
        # Show full JSON
        print(json.dumps(issue_data, indent=2))
        return
    
    # Extract key fields
    issue_key = issue_data.get('key')
    fields = issue_data.get('fields', {})
    
    summary = fields.get('summary', 'No summary')
    description = fields.get('description', 'No description')
    status = fields.get('status', {}).get('name', 'Unknown')
    issue_type = fields.get('issuetype', {}).get('name', 'Unknown')
    priority = fields.get('priority', {}).get('name', 'No priority')
    
    # Assignment data
    assignee = fields.get('assignee')
    assignee_name = assignee.get('displayName') if assignee else "Unassigned"
    
    # Important dates
    created = fields.get('created', 'Unknown')
    updated = fields.get('updated', 'Unknown')
    
    if output_format == "simple":
        print(f"Issue: {issue_key}")
        print(f"Title: {summary}")
        print(f"Status: {status}")
        print(f"Type: {issue_type}")
        print(f"Priority: {priority}")
        print(f"Assigned to: {assignee_name}")
    else:  # detailed format
        print("=" * 80)
        print(f"Issue: {issue_key} - {summary}")
        print("-" * 80)
        print(f"Type: {issue_type}")
        print(f"Status: {status}")
        print(f"Priority: {priority}")
        print(f"Assigned to: {assignee_name}")
        print(f"Created: {created}")
        print(f"Updated: {updated}")
        print("-" * 80)
        print("Description:")
        print(description if description else "No description")
        print("-" * 80)
        
        # Show additional fields in detailed format
        components = fields.get('components', [])
        if components:
            print("Components:")
            for component in components:
                print(f"- {component.get('name', '')}")
            print("-" * 80)
        
        # Show labels if they exist
        labels = fields.get('labels', [])
        if labels:
            print("Labels:")
            print(", ".join(labels))
            print("-" * 80)
        
        # Show sprint information if available
        sprint_field = None
        for field_name, field_value in fields.items():
            if field_name.lower().endswith('sprint') and field_value:
                sprint_field = field_value
                break
        
        if sprint_field:
            print("Sprint:")
            if isinstance(sprint_field, list):
                for sprint in sprint_field:
                    if isinstance(sprint, str):
                        print(f"- {sprint}")
                    else:
                        print(f"- {sprint.get('name', 'No name')}")
            else:
                print(f"- {sprint_field}")
            print("-" * 80)
        
        # Show links to other issues
        issue_links = fields.get('issuelinks', [])
        if issue_links:
            print("Links to other issues:")
            for link in issue_links:
                if 'outwardIssue' in link:
                    link_type = link.get('type', {}).get('outward', 'related to')
                    linked_issue = link.get('outwardIssue', {})
                    linked_key = linked_issue.get('key', '')
                    linked_summary = linked_issue.get('fields', {}).get('summary', '')
                    print(f"- {link_type} {linked_key}: {linked_summary}")
                elif 'inwardIssue' in link:
                    link_type = link.get('type', {}).get('inward', 'related to')
                    linked_issue = link.get('inwardIssue', {})
                    linked_key = linked_issue.get('key', '')
                    linked_summary = linked_issue.get('fields', {}).get('summary', '')
                    print(f"- {link_type} {linked_key}: {linked_summary}")
            print("-" * 80)

def main():
    """
    Main function that processes arguments and gets issue information.
    """
    # Configure argument parser
    parser = argparse.ArgumentParser(
        description="Get information about a specific Jira issue"
    )
    
    parser.add_argument(
        "issue_key", 
        help="Key of the issue to query (eg: PROJ-123)"
    )
    
    
    parser.add_argument(
        "-o", "--output",
        choices=["simple", "json", "detailed"],
        default="detailed",
        help="Output format (default: detailed)"
    )
    
    parser.add_argument(
        "--env",
        help="Path to .env file with credentials"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Load environment variables
    if not load_env_vars(args.env):
        logger.error("Could not load environment variables.")
        return 1
    
    # Get and show issue
    issue_data = get_issue(args.issue_key)
    
    if issue_data:
        show_issue(issue_data, args.output)
        return 0
    else:
        logger.error(f"Could not get information for issue {args.issue_key}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
