# 11. Write a python program to rename a file to "renamed_by_python.txt".

with open("./Learn-Python/Chapter-09/Practice-Set/rename.txt") as f:
    content = f.read()


with open("./Learn-Python/Chapter-09/Practice-Set/renamed_by_python.txt", "w") as f:
    f.write(content)


# ............ Blackbox result ............

# import os

# # Specify the current file name and the new file name
# current_file_name = "./Learn-Python/Chapter-09/Practice-Set/rename.txt"  # Replace with your actual file name
# new_file_name = "./Learn-Python/Chapter-09/Practice-Set/rename_by_python.txt"

# try:
#     # Rename the file
#     os.rename(current_file_name, new_file_name)
#     print(f"File renamed to {new_file_name}")
# except FileNotFoundError:
#     print(f"The file {current_file_name} does not exist.")