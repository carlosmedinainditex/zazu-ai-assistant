import os
import json
import datetime
from pathlib import Path


def save_to_file(content, output_dir, ext, prefix="output"):
    """
    Save content to a file in output_dir with a timestamp and prefix. Returns the output path.
    """
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_filename = f"{prefix}_{now}.{ext}"
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    return output_path

def print_json_and_save(elements, output_dir="reports/json", prefix="output", jql_query=None):
    """
    Print elements as JSON and save to a file in output_dir. Optionally include JQL in the file as a comment.
    """
    json_content = json.dumps(elements, indent=2, ensure_ascii=False)
    if jql_query:
        json_content = f"// JQL: {jql_query}\n" + json_content
    output_path = save_to_file(json_content, output_dir, "json", prefix)
    print(json_content)
    print(f"\nArchivo generado: {output_path}")
    return output_path

def print_markdown_table_and_save(elements, output_dir="reports/markdown/table", prefix="output", jql_query=None):
    """
    Print elements as a Markdown table and save to a file in output_dir. Optionally include JQL in the file.
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
    md_content = f"# Resultados JQL\n\n"
    if jql_query:
        md_content += f"**JQL ejecutada:** `{jql_query}`\n\n"
    md_content += "\n".join(table_lines)
    output_path = save_to_file(md_content, output_dir, "md", prefix)
    print(md_content)
    print(f"\nArchivo generado: {output_path}")
    return output_path

def print_markdown_list_and_save(elements, output_dir="reports/markdown/list", prefix="output", jql_query=None):
    """
    Print elements as a nested Markdown list and save to a file in output_dir. Optionally include JQL in the file.
    """
    def md_list(element, level=0):
        indent = "  " * level
        line = f"{indent}- **{element['id']}**: {element['title']} ({element['status']})\n"
        line += f"{indent}  - Descripción: {element['description'][:60]}\n"
        line += f"{indent}  - Asignado: {element['assignee']} | Reportero: {element['reporter']}\n"
        line += f"{indent}  - Creado: {element['created']} | Entrega: {element['duedate']}\n"
        for child in element.get('children', []):
            line += md_list(child, level+1)
        return line
    md_lines = [f"# Resultados JQL\n\n"]
    if jql_query:
        md_lines.append(f"**JQL ejecutada:** `{jql_query}`\n\n")
    for element in elements:
        md_lines.append(md_list(element))
    md_content = "".join(md_lines)
    output_path = save_to_file(md_content, output_dir, "md", prefix)
    print(md_content)
    print(f"\nArchivo generado: {output_path}")
    return output_path
