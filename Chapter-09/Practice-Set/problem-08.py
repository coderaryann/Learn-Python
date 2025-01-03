# 8. Write a program to make a copy of a text file "this.txt"

with open("./Learn-Python/Chapter-09/Practice-Set/this.txt") as f:
    content = f.read()

with open("./Learn-Python/Chapter-09/Practice-Set/this_copy2.txt", "w") as f:
    f.write(content)