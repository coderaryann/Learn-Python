# 9. Write a program to find out whether a file is identical & matches the content of another file.

# with open("./Learn-Python/Chapter-09/Practice-Set/log.txt") as f:  # Not identical
with open("./Learn-Python/Chapter-09/Practice-Set/this.txt") as f:  # Yes identical
    content1 = f.read()
    
with open("./Learn-Python/Chapter-09/Practice-Set/this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are identical")