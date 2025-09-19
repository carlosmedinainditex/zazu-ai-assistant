# Environment Configuration

This directory contains environment configuration files for Jira scripts.

## Files

- `.env`: Main file with credentials and configuration (not included in the repository)
- `.env.example`: Example template to create the `.env` file

## Configuration

To configure the scripts:

1. Copy `.env.example` to `.env`
2. Edit `.env` with your Jira credentials
3. Make sure the `.env` file is not included in version control

## Environment Variables

- `JIRA_SERVER`: Jira server URL (e.g., https://jira.example.com)
- `JIRA_USER`: Your Jira username
- `JIRA_TOKEN`: Your Jira API token (using an API token is recommended instead of a password)

## Optional Variables

- `HTTP_PROXY`, `HTTPS_PROXY`: Proxy configuration if needed
- `NO_PROXY`: Domains that should bypass the proxy
