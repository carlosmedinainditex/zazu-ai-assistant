import os
import json
import datetime
from pathlib import Path


def save_to_file(content, output_dir, ext, prefix="output", custom_timestamp=None):
    """
    Save content to a file in output_dir with a timestamp and prefix. Returns the output path.
    
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
    output_path = save_to_file(json_content, output_dir, "json", prefix, custom_timestamp)
    print(f"Generate file: {output_path}")
    return output_path

def save_markdown_table_to_file(elements, jql_query, output_dir="reports/markdown/table", prefix="output", custom_timestamp=None):
    """
    Save elements as a Markdown table to a file in output_dir, including JQL in the file.
    
    Args:
        elements: Data to format as markdown table
        jql_query: JQL query to include in the file
        output_dir: Output directory
        prefix: File prefix
        custom_timestamp: Custom timestamp for filename (if None, uses current time)
    """
    headers = ["ID", "Título", "Descripción", "Estado", "Asignado", "Reportero", "Creado", "Fecha Entrega"]
    table_lines = []
    table_lines.append("|" + "|".join(headers) + "|")
    table_lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for f in elements:
        row = [
            str(f["id"] or ""),
            str(f["title"] or "").replace("|", "/"),
            str((f["description"] or '')).replace("\n", " ").replace("|", "/")[:80],
            str(f["status"] or ""),
            str(f["assignee"] or ""),
            str(f["reporter"] or ""),
            str(f["created"] or ""),
            str(f["duedate"] or "")
        ]
        table_lines.append("|" + "|".join(row) + "|")
    md_content = f"# JQL Results\n\n**JQL triggered:** `{jql_query}`\n\n"
    md_content += "\n".join(table_lines)
    output_path = save_to_file(md_content, output_dir, "md", prefix, custom_timestamp)
    print(f"Generated file: {output_path}")
    return output_path

def save_markdown_list_to_file(elements, jql_query, output_dir="reports/markdown/list", prefix="output", custom_timestamp=None):
    """
    Save elements as a nested Markdown list to a file in output_dir, including JQL in the file.
    
    Args:
        elements: Data to format as markdown list
        jql_query: JQL query to include in the file
        output_dir: Output directory
        prefix: File prefix
        custom_timestamp: Custom timestamp for filename (if None, uses current time)
    """
    def md_list(element, level=0):
        indent = "  " * level
        line = f"{indent}- **{element['id']}**: {element['title']} ({element['status']})\n"
        line += f"{indent}  - Descripción: {(element['description'] or '')[:60]}\n"
        line += f"{indent}  - Asignado: {element['assignee']} | Reportero: {element['reporter']}\n"
        line += f"{indent}  - Creado: {element['created']} | Entrega: {element['duedate']}\n"
        for child in element.get('children', []):
            line += md_list(child, level+1)
        return line
    md_lines = [f"# JQL Results\n\n**JQL triggered:** `{jql_query}`\n\n"]
    for element in elements:
        md_lines.append(md_list(element))
    md_content = "".join(md_lines)
    output_path = save_to_file(md_content, output_dir, "md", prefix, custom_timestamp)
    print(f"Generated file: {output_path}")
    return output_path
