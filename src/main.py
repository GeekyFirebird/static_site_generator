import os
import shutil

from copy_static import copy_files_recursive

# Source - Static
# Destination - Public

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):  # If the destination exists
        shutil.rmtree(dir_path_public) # remove it for a clean copy

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public) #Run copy files method
    

main()

