#!/usr/bin/env python3
"""
Diagnostic script to test Jira connection.
Uses direct HTTP requests to test the connection to the Jira server.
"""

import os
import sys
import logging
import requests
from pathlib import Path

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

logger = logging.getLogger("JiraDiagnostic")

def test_http_connection():
    """
    Test the basic HTTP connection to the Jira server.
    """
    try:
        # Get credentials
        jira_server = os.environ.get("JIRA_SERVER", "").strip()
        jira_user = os.environ.get("JIRA_USER", "").strip()
        jira_token = os.environ.get("JIRA_TOKEN", "").strip()
        
        # Verify we have the credentials
        if not jira_server:
            logger.error("Missing Jira server URL (JIRA_SERVER)")
            return False
        if not jira_user:
            logger.error("Missing Jira user (JIRA_USER)")
            return False
        if not jira_token:
            logger.error("Missing Jira token (JIRA_TOKEN)")
            return False
        
        # Make sure URL doesn't end with /
        if jira_server.endswith('/'):
            jira_server = jira_server[:-1]
        
        # URLs to test
        urls_to_test = [
            f"{jira_server}/rest/api/2/myself",  # Standard API
            f"{jira_server}/rest/api/3/myself",  # API v3
            f"{jira_server}/rest/api/latest/myself"  # API latest
        ]
        
        # Define headers for Bearer Token authentication
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {jira_token}"
        }
        
        successful_url = None
        
        # Try each URL until we find one that works
        for url in urls_to_test:
            logger.info(f"Testing connection to: {url}")
            
            try:
                # Make request with Bearer Token authentication
                response = requests.get(url, headers=headers, timeout=10)
                
                # Show response code
                logger.info(f"Response code: {response.status_code}")
                
                # If the response is successful, show user data
                if response.status_code == 200:
                    user_data = response.json()
                    logger.info(f"Connection successful! Connected as: {user_data.get('displayName', user_data.get('name', 'Unknown'))}")
                    
                    # Show basic user info
                    logger.info(f"Username: {user_data.get('name')}")
                    logger.info(f"Email: {user_data.get('emailAddress', 'N/A')}")
                    
                    # Store successful URL
                    successful_url = url
                    logger.info(f"Working API endpoint: {successful_url}")
                    return True
                else:
                    logger.warning(f"Request failed with status {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                logger.error(f"HTTP connection error: {str(e)}")
        
        # If we reach here, no URLs worked
        logger.error("Could not connect to any of the Jira API URLs")
        
        # Try a simple connection to verify server accessibility
        try:
            logger.info(f"Trying basic connection to {jira_server} (without authentication)...")
            response = requests.get(jira_server, timeout=5, allow_redirects=True)
            
            if response.status_code < 400:
                logger.info("The Jira server seems to be accessible, but there are problems with authentication or the API")
            else:
                logger.error(f"The server responded with an error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Could not connect to the Jira server: {str(e)}")
            
        return False
    
    except Exception as e:
        logger.error(f"Unexpected error while testing the connection: {str(e)}")
        return False

def main():
    """
    Main function that runs the diagnostic tests.
    """
    logger.info("=== Starting Jira connection diagnostic ===")
    
    # Load environment variables
    if not load_env_vars():
        logger.error("Could not load environment variables. Make sure you have a valid .env file.")
        return 1
    
    # Show environment variables (without showing the token)
    jira_server = os.environ.get("JIRA_SERVER", "").strip()
    jira_user = os.environ.get("JIRA_USER", "").strip()
    
    logger.info(f"Jira server URL: {jira_server}")
    logger.info(f"Jira user: {jira_user}")
    
    # Test HTTP connection
    result = 0 if test_http_connection() else 1
    
    logger.info("=== Diagnostic finished ===")
    return result

if __name__ == "__main__":
    sys.exit(main())
