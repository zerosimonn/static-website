import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

# Check if basepath is provided for URLs
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

# Define file system paths (without basepath)
dir_path_static = "static"  # Local file system path
dir_path_public = "docs"  
dir_path_content = "content"
template_path = "template.html"

# main script
def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )

main()