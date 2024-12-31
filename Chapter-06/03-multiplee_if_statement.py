a = int(input("Enter your age: "))

# statement 1
if (a%2 == 0):
    print("age is even")

# statement 2
if (a >= 18):
    print("You're above the age of consent")

elif (a <= 0):
    print("You're entering an invalid age!")

else:
    print("You're below the age of consent")
