'''
factorial(0) = 1
factorial(1) = 1
factorial(3) = 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x (n-1) x .......3 x 2 x 1

factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

num = int(input("Enter the number: "))
print(f"The factorial of {num} is: {factorial(num)}")