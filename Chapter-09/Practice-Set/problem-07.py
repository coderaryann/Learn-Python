# 7. Write a program to find out the line number where python is present from ques 6.

with open("./Learn-Python/Chapter-09/Practice-Set/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python word is present in log file, Line no. {lineno}")
        break
    lineno += 1

else:
    print("No, python word is not present in log file")