import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html()

    title = extract_title(markdown_content)
    
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(html)
    to_file.close()
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, os.path.join(dest_dir_path, entry), basepath)
        elif os.path.isfile(entry_path):
            if entry.endswith(".md"):
                path = os.path.join(dest_dir_path, entry)
                os.makedirs(dest_dir_path, exist_ok=True)
                generate_page(entry_path, template_path, path.replace(".md", ".html"), basepath)
        else:
            print(f"Not dir and not .md {entry_path}")


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")