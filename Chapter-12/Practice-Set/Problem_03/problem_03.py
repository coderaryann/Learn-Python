# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter any number, you wanna print table of the number: "))

table = [n*i for i in range(1, 11)]
print(table)