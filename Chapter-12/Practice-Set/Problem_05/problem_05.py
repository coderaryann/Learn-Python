# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter any number, you wanna print table of the number: "))

table = [n*i for i in range(1, 11)]
print(table)

with open ("../LEARN-PYTHON/Chapter-12/Practice-Set/Problem_05/tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")