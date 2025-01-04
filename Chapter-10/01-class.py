class Emlpoyee:
    language = "Python"  # This is a class attribute
    salary = 2

data1 = Emlpoyee()
data1.name = "Aryan"  # This is an instance attribute
print(data1.name, data1.language, data1.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class