#!/usr/bin/env python3
"""
Utility functions for running scripts and commands.
"""

import sys
import subprocess
from pathlib import Path

# Get the script directory path (parent of utils)
SCRIPT_DIR = Path(__file__).parent.parent.absolute()

# Add config directory to the Python path to import the colors module
sys.path.append(str(SCRIPT_DIR))

# Import colors directly from the colors.py module
from config.colors import YELLOW, NC

def run_script(script_path, *args):
    """
    Runs a Python script with additional arguments
    
    Args:
        script_path: Path to the script to execute
        *args: Additional arguments for the script
    """
    cmd = [sys.executable, str(script_path)] + list(args)
    subprocess.run(cmd)
    input(f"\n{YELLOW}Press ENTER to continue...{NC}")

def run_shell_command(command, show_output=True):
    """
    Runs a shell command
    
    Args:
        command: Command to execute
        show_output: Whether to display the command output
    """
    if show_output:
        subprocess.run(command, shell=True)
    else:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
