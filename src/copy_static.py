import os
import shutil

# Source - Static
# Destination - Public

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path): #If the file path does not exist, 
        os.mkdir(dest_dir_path) #Make it
    
    for filename in os.listdir(source_dir_path): # For each file in the source dir
        from_path = os.path.join(source_dir_path, filename) #Creates a source path for the file
        dest_path = os.path.join(dest_dir_path, filename) # Creates a destination path for the file
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path): # If the file is actually a file
            shutil.copy(from_path, dest_path) #Move the file to the destination path
        else:
            copy_files_recursive(from_path, dest_path) #If the file is not a file (a folder) loop back through the method 
