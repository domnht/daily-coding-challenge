# File: libs/setup_test.py

import os
import shutil
import sys
from pathlib import Path

# --- Configuration ---
# The root of the repository (one level up from libs/)
BASE_DIR = Path(__file__).parent.parent 
CHALLENGES_DIR = BASE_DIR / "challenges"
SOURCE_MODULE = BASE_DIR / "libs" / "module_test.py"
TARGET_FILENAME = "module_test.py"


def find_target_directories(root_dir: Path) -> list[Path]:
    """
    Finds all subdirectories that contain a 'solution.py' file.
    These are considered the individual challenge folders.
    """
    target_dirs = []
    # os.walk traverses the directory tree
    for root, dirs, files in os.walk(root_dir):
        # The presence of solution.py marks a challenge directory
        if "solution.py" in files:
            target_dirs.append(Path(root))
    return target_dirs

def setup_tests():
    """Copies module_test.py to all challenge directories."""
    print("--- Starting Test Module Setup (Copy) ---")
    
    if not SOURCE_MODULE.exists():
        print(f"ERROR: Source file not found at {SOURCE_MODULE}. Ensure libs/module_test.py exists.")
        return

    target_dirs = find_target_directories(CHALLENGES_DIR)
    
    if not target_dirs:
        print("No challenge directories (containing solution.py) found to copy to.")
        return

    for target_dir in target_dirs:
        destination = target_dir / TARGET_FILENAME
        
        # shutil.copy2 copies the file, including metadata
        shutil.copy2(SOURCE_MODULE, destination)
        print(f"Copied to: {destination.relative_to(BASE_DIR)}")

    print("--- Setup COMPLETE ---")

def clean_tests():
    """Deletes all copies of module_test.py from challenge directories."""
    print("--- Starting Test Module Cleanup (Delete) ---")

    target_dirs = find_target_directories(CHALLENGES_DIR)
    
    if not target_dirs:
        print("No challenge directories found to clean up.")
        return

    for target_dir in target_dirs:
        file_to_delete = target_dir / TARGET_FILENAME
        
        if file_to_delete.exists():
            # os.remove deletes the file
            os.remove(file_to_delete)
            print(f"Deleted: {file_to_delete.relative_to(BASE_DIR)}")

    print("--- Cleanup COMPLETE ---")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python libs/setup_test.py [setup|clean]")
        sys.exit(1)
        
    command = sys.argv[1].lower()

    if command == "setup":
        setup_tests()
    elif command == "clean":
        clean_tests()
    else:
        print(f"Invalid command: {sys.argv[1]}. Use 'setup' or 'clean'.")
        sys.exit(1)
