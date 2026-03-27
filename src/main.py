import os
import shutil
import sys

from copy_static import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

# Source - Static
# Destination - Public

dir_path_static = "./static"
dir_path_public = "./docs"

dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):  # If the destination exists
        shutil.rmtree(dir_path_public) # remove it for a clean copy

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public) #Run copy files method
    
    print("Generating Page...")
    generate_pages_recursive(
        dir_path_content, 
        template_path, 
        dir_path_public, 
        basepath
    )
    # generate_page("content/index.md", "template.html", "public/index.html")

main()

