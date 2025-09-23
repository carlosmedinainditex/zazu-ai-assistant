import os
import json
import datetime
from pathlib import Path


def save_to_file(content, output_dir, ext, prefix="output", custom_timestamp=None):
    """
    Save content to a file in output_dir with a timestamp and prefix. Returns the output path.
    Prints confirmation message.
    
    Args:
        content: Content to save
        output_dir: Directory to save the file
        ext: File extension
        prefix: File prefix
        custom_timestamp: Optional custom timestamp string. If None, uses current time.
    """
    timestamp = custom_timestamp or datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_filename = f"{prefix}_{timestamp}.{ext}"
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated file: {output_path}")
    return output_path

def save_json_to_file(elements, jql_query, output_dir="reports/json", prefix="output", custom_timestamp=None):
    """
    Save elements as JSON to a file in output_dir, including JQL as a comment.
    
    Args:
        elements: Data to save as JSON
        jql_query: JQL query to include as comment
        output_dir: Output directory
        prefix: File prefix
        custom_timestamp: Custom timestamp for filename (if None, uses current time)
    """
    json_content = json.dumps(elements, indent=2, ensure_ascii=False)
    json_content = f"// JQL: {jql_query}\n" + json_content
    return save_to_file(json_content, output_dir, "json", prefix, custom_timestamp)
