from textnode import TextNode, TextType, extract_title
from markdown_blocks import markdown_to_html_node
from htmlnode import *
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    # Get the directory where your script is running from
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up one directory from src to the project root
    project_root = os.path.dirname(current_dir)
    # Build absolute paths to source and destination
    source_dir = os.path.join(project_root, "static")
    dest_dir = os.path.join(project_root, "public")
    # Call your copy function with absolute paths
    copy_static(source_dir, dest_dir)
        # Generate the page from content/index.md
    content_path = os.path.join(project_root, "content/index.md")
    template_path = os.path.join(project_root, "template.html")
    dest_path = os.path.join(project_root, "public/index.html")
    generate_page(content_path, template_path, dest_path)

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    htmlnode = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", htmlnode)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    with open(dest_path, "w") as f:
        f.write(template)

main()

