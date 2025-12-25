# This is a script to rename a lot of files in a directory
import os
import re

def rename_files(directory, str_old, str_new):
    for filename_old in os.listdir(directory):
        if re.search(rf'{str_old}', filename_old):
            filename_new = re.sub(rf'{str_old}', rf'{str_new}', filename_old)
            path_old = os.path.join(directory, filename_old)
            path_new = os.path.join(directory, filename_new)
            if not os.path.exists(path_new):
                os.rename(path_old, path_new)
                print(f"Renaming '{filename_old}' to '{filename_new}'")

# Example usage:
# rename_files("/path/to/directory", "search", "old", "new")
if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    str_old = input("Enter the string to be replaced: ")
    str_new = input("Enter the new string: ")
    rename_files(dir_path, str_old, str_new)
    print("Files renamed successfully.")