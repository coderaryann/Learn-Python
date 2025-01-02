def greet (name, lastname="kumar"):
    print("Good day,", name, lastname)
    return "Thanks"

a = greet("Rahul")
print(a)
b = greet("Rahul", "Jaiswal")
print(b)