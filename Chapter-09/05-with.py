# f = open("./Learn-Python/Chapter-09/file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:

with open("./Learn-Python/Chapter-09/file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file