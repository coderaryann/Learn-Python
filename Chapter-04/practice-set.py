# 1. Write a program to store seven marks in a list entered by the user.
print("Q. no. 1 solution.")

fruits = []

f1 = input("Enter fruits name: ")
fruits.append(f1)
f2 = input("Enter fruits name: ")
fruits.append(f2)
f3 = input("Enter fruits name: ")
fruits.append(f3)
f4 = input("Enter fruits name: ")
fruits.append(f4)
f5 = input("Enter fruits name: ")
fruits.append(f5)
f6 = input("Enter fruits name: ")
fruits.append(f6)
f7 = input("Enter fruits name: ")
fruits.append(f7)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
print("Q. no. 2 solution.")

marks = []

f1 = int(input("Enter your marks here: "))
marks.append(f1)
f2 = int(input("Enter your marks here: "))
marks.append(f2)
f3 = int(input("Enter your marks here: "))
marks.append(f3)
f4 = int(input("Enter your marks here: "))
marks.append(f4)
f5 = int(input("Enter your marks here: "))
marks.append(f5)
f6 = int(input("Enter your marks here: "))
marks.append(f6)

marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.
print("Q. no. 3 solution.")

# a = (34, "name", 434)
# a[2] = "f-name"
# print(a)

# 4. Write a program to sum a list with 4 numbers.
print("Q. no. 4 solution.")

list = [4, 5, 7, 3]
print(sum(list))

# Write a program to count the number of zeros in the following tuple:  a = (7, 0, 8, 0, 0, 9)
print("Q. no. 5 solution.")

a = (7, 0, 8, 0, 0, 9)

print(a.count(0))