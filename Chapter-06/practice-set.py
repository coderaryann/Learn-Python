# 01. Write a program to find the greatest of four entered by the user.
print("Q. no. 1 solution.")

a1  = int(input("Enter number 1: "))
a2  = int(input("Enter number 2: "))
a3  = int(input("Enter number 3: "))
a4  = int(input("Enter number 4: "))

if (a1>a2 and a3<a1 and a4<a1):
    print("Greatest number is:", a1)

elif (a1<a2 and a3<a2 and a4<a2):
    print("Greatest number is:", a2)

elif (a1<a3 and a2<a3 and a4<a3):
    print("Greatest number is:", a3)

elif (a1<a4 and a2<a4 and a3<a4):
    print("Greatest number is:", a4)

# 02. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
print("Q. no. 2 solution.")

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# total marks & percentage
total_marks = marks1 + marks2 + marks3
total_percentage = ((total_marks) / 300) * 100

# check total percentage of marks
if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You Passed,", "Your percentage is:", total_percentage)
else:
    print("You failed,", "Your percentage is:", total_percentage)


# 03. A spam comment is defined as a text containing following keywords:
# * "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
print("Q. no. 3 solution.")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam comment")

else:
    print("This is not a spam comment")

# 04. Write a program to find whether a given username contians less than 10 characters or not.
print("Q. no. 4 solution.")

username = input("Enter your name: ")

if (len(username) < 10):
    print("Your username contians less than 10 characters")

else:
    print("Your username contians more than 10 characters")

# 05. Write a program which finds out whether a given name is present in a list or not.
print("Q. no. 5 solution.")

l = ["Harry", "Rohan", "Sumit", "Rahul", "Priya", "Divya", "Divyam"]

name = input("Enter your name: ")

if (name in l):
    print(name)

else:
    print("User not found")

# 06. Write a program to calculate the grade of a student from his marks from the following scheme:
# * 90 - 100 => Ex
# * 80 - 90 => A
# * 70 - 80 => B
# * 60 - 70 => C
# * 50 - 60 => D
# * <50 => F
print("Q. no. 6 solution.")

marks = int(input("Enter your marks: "))

if (marks >= 90 and marks < 100):
    grade = "EX"

elif (marks >= 80 and marks < 90):
    grade = "A"

elif (marks >= 70 and marks < 80):
    grade = "B"

elif (marks >= 60 and marks < 70):
    grade = "C"

elif (marks >= 50 and marks < 60):
    grade = "D"

elif (marks < 50):
    grade = "F"
    
print("Your grade is:", grade)

# 07. Write a program to find out whether a given post is talking about "Good" or not.
print("Q. no. 7 solution.")

post = input("Enter the post: ")

if ("good" in post.lower()):
    print("This post is talking about good")

else:
    print("This post is not talking about good")