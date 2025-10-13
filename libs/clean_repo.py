import os
import shutil
import sys
from pathlib import Path

def cleanup_python_project(path_to_clean: str = '.'):
    """
    Cleans up common Python temporary/junk directories and files 
    (like __pycache__, .pyc, and virtual environments).

    Args:
        path_to_clean: The root directory path to clean. Defaults to 
                       the current directory ('.').
    """

    # Resolve to the absolute path for clear printing
    root_path = Path(path_to_clean).resolve()
    print(f"--- Starting cleanup in: {root_path} ---")

    # 1. Define targets for deletion
    # Common junk directories: pycache, and virtual environment folders
    target_dirs = ["__pycache__", ".venv", "venv", "env"]
    # Common junk file extensions
    target_files_extensions = [".pyc"]

    items_deleted_count = 0

    # os.walk traverses the directory tree. topdown=False ensures we delete 
    # contents before the parent directory, which is essential for rmtree to work.
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        current_dir = Path(dirpath)

        # --- A. Delete common junk directories (e.g., __pycache__, venv) ---
        # We use list(dirnames) to iterate, so we can modify the actual dirnames
        # list later to prevent os.walk from entering deleted folders.
        for dir_name in list(dirnames): 
            
            if dir_name in target_dirs:
                dir_to_delete = current_dir / dir_name
                
                try:
                    # Remove the directory and all its contents recursively
                    shutil.rmtree(dir_to_delete)
                    print(f"Deleted directory: {dir_to_delete.relative_to(root_path)}")

                    # Remove from dirnames list so os.walk skips descending into it
                    dirnames.remove(dir_name) 
                    items_deleted_count += 1
                except OSError as e:
                    print(f"Error deleting {dir_to_delete}: {e}")

        # --- B. Delete compiled files (.pyc) ---
        for file_name in filenames:
            for ext in target_files_extensions:
                if file_name.endswith(ext):
                    file_to_delete = current_dir / file_name
                    
                    try:
                        os.remove(file_to_delete)
                        print(f"Deleted file: {file_to_delete.relative_to(root_path)}")
                        items_deleted_count += 1
                    except OSError as e:
                        print(f"Error deleting file {file_to_delete}: {e}")

    print("\n------------------------------")
    if items_deleted_count > 0:
        print(f"Cleanup finished. Total {items_deleted_count} items deleted.")
    else:
        print("No items found for cleanup.")
    print("------------------------------")

# --- Usage Example ---
if __name__ == "__main__":
    # If a path argument is provided, use it. Otherwise, use the current directory.
    if len(sys.argv) > 1:
        cleanup_python_project(sys.argv[1])
    else:
        cleanup_python_project()
