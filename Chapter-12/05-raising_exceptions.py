a = int(input("Enter first number: "))
b = int(input("Enter secondnumber: "))

if (b == 0):
  raise ZeroDivisionError ("Our program is not meant to divide numbers by 'zero'")

else:
  print(f"The division of a/b is {a/b}")