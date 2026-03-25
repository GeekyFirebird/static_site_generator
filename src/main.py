import os
import shutil

from copy_static import copy_files_recursive
from gencontent import generate_page

# Source - Static
# Destination - Public

dir_path_static = "./static"
dir_path_public = "./public"

dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):  # If the destination exists
        shutil.rmtree(dir_path_public) # remove it for a clean copy

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public) #Run copy files method
    
    print("Generating Page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
    # generate_page("content/index.md", "template.html", "public/index.html")

main()

