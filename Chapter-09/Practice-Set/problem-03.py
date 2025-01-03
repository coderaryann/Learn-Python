# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place dthese files in a folder for a 13 - year old.

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*1}\n"

    with open(f"./Learn-Python/Chapter-09/Practice-Set/tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)