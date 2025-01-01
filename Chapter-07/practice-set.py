# 1. Write a program to print multiplication table of a given number using for loop.
print("Q. no. 1 solution.")

num = int(input("Enter any number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
print("Q. no. 2 solution.")

l = ["Harry", "Soham", "Sachin", "Rahul"]

for n in l:
    if (n.startswith("S")):
        print(f"Hello, {n}")

# 3. Attempt problem 1 using while loop.
print("Q. no. 3 solution.")

num = int(input("Enter any number: "))

i = 1
while (i <= 10):
    print(f"{num} x {i} = {num * i}")
    i += 1

# 4. Write a program to find whether a given number is prime or not.
print("Q. no. 4 solution.")

num = int(input("Enter any number: "))

for i in range ( 2, num):
    if (num % i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")


# 5. Write a program to find the sum of first n natural numbers using while loop.
print("Q. no. 5 solution.")

num = int(input("Enter any number: "))
i = 1
sum = 0
while (i <= num):
    sum += i
    i += 1
print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.
print("Q. no. 6 solution.")

# 5! = 1 x 2 x 3 x 4 x 5

num = int(input("Enter any number: "))
product = 1

for i in range(1, num+1):
    product = product * i

print(f"The factorial of {num} is {product}")

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
print("Q. no. 7 solution.")

'''

For n = 3
  *
 ***
*****

'''

num = int(input("Enter the number: "))

for i in range (1, num + 1):
    print(" "* (num - i), end="")
    print("*"* (2 * i - 1), end="")
    print("")


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
print("Q. no. 8 solution.")

num = int(input("Enter the number: "))

for i in range (1, num + 1):
    # print(" "* (num - i), end="")
    print("*"* i, end="")
    print("")

# 9. Write a program to print the following star pattern:
# ***
# * * for n = 3
# ***
print("Q. no. 9 solution.")

num = int(input("Enter the number: "))

for i in range (1, num + 1):
    if(i == 1 or i == num):
        print("*"* num, end="")

    else:
        print("*", end="")
        print(" "* (num - 2), end="")
        print("*", end="")
    print("")

# 10. Write a program to print multiplication table of n using for loops in reversed order.
print("Q. no. 10 solution.")

num = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{num} x {11 - i} = {num*(11 - i)}")