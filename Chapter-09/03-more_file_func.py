f = open("./Learn-Python/Chapter-09/file.txt")

# lines = f.readlines()
# print(lines, type(lines))


# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# line5 = f.readline()
# print(line5)
# print(line5 == "")

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()