#!/usr/bin/env python3
"""
Utility for loading environment variables from .env files.
This module is used across the application to ensure consistent loading of environment variables.
"""

import os
import logging
from pathlib import Path

logger = logging.getLogger("EnvLoader")

def load_env_vars(env_file=None):
    """
    Load environment variables from a .env file.
    
    Args:
        env_file (str, optional): Path to the .env file. If None, it will look in standard locations.
    
    Returns:
        bool: True if environment variables were loaded successfully, False otherwise.
    """
    if env_file is None:
        # Simple project root detection based on common directories
        project_root = Path().absolute()
        
        # Check standard locations for .env file in priority order
        possible_locations = [
            project_root / "env" / ".env",  # Standard location: /path/to/project/env/.env
            project_root / ".env",          # Alternative: /path/to/project/.env
            Path(".env")                    # Local directory: .env
        ]
        
        for loc in possible_locations:
            if loc.is_file():
                env_file = str(loc)
                break
        
        if env_file is None:
            logger.error("No .env file found in standard locations")
            return False
    
    try:
        # Read and process the .env file
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                
                # Skip empty lines or comments
                if not line or line.startswith("#"):
                    continue
                
                # Extract and set environment variables
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove surrounding quotes if present
                    if (value.startswith('"') and value.endswith('"')) or \
                       (value.startswith("'") and value.endswith("'")):
                        value = value[1:-1]
                    
                    os.environ[key] = value
        
        return True
    
    except Exception as e:
        logger.error(f"Error loading environment variables: {str(e)}")
        return False
