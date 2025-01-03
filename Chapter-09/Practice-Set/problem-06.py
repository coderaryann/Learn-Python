# 6. Write a program to mine a log file and find out whether it contains 'python'.

with open("./Learn-Python/Chapter-09/Practice-Set/log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes, python word is present in log file")
else:
    print("No, python word is not present in log file")