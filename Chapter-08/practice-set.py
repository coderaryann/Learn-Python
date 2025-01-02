# 1. Write a program using functions to find greatest of three numbers.
print("Q. no. 1 solution.")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def greatest (a, b, c):
    if (a > b and a > c):
        return f"The greatest number is: {a}"
    elif (b > a and b > c):
        return f"The greatest number is: {b}"
    elif (c > a and c > b):
        return f"The greatest number is: {c}"

print (greatest(a, b, c))


# 2. Write a python program using function to convert Celsuis to Fahrenheit
print("Q. no. 2 solution.")

def f_to_c(f):
    return 5 * (f-32) / 9

f = int(input("Enter temperature in °F: "))
cal = f_to_c(f)
print(f"{round(cal, 2)}°C")

# 3. How do you prevent a python print() function to print a new line at the end.
print("Q. no. 3 solution.")

print("a")
print("b")
print("c", end="")
print("d", end="")

# 4. Write a recursive function to calculate the sum of first n natural numbers.
print("Q. no. 4 solution.")

num = int(input("Enter a number: "))

def sum (n):
    if (n == 1):
        return 1
    return n + sum (n-1)

print (sum(num))


# 5. Write a python function to print first n lines of the following pattern:
#  ***
#  **       - for n = 3
#  *
print("Q. no. 5 solution.")

def pattern(n):
    if (n == 0):
        return
    
    print("*" * n)
    pattern(n-1)

pattern(3)

# 6. Write a python function which converts inches to cms.
print("Q. no. 6 solution.")

def converter(i):
    return i * 2.54

num = int(input("Enter a number: "))
print(f"{converter(num)}cm")

# 7. Write a python function to remove a given word from a list ad strip it at the same time.
print("Q. no. 7 solution.")

def rem (l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
    
l = ["Harry", "Portor", "Rohan", "Shubham", "an"]

print(rem(l, "an"))

# 8. Write a python function to print multiplication table of a given number.
print("Q. no. 8 solution.")

num = int(input("Enter a number: "))
def table (n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    
table(num)