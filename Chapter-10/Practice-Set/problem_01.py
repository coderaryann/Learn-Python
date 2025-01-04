# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

dev1 = Programmer("Aryan", "40LPA")
print(f"Company Name: {dev1.company}\nDeveloper Name: {dev1.name}\nSalary: {dev1.salary}\n")

dev2 = Programmer("Rohan", "10LPA")
print(f"Company Name: {dev2.company}\nDeveloper Name: {dev2.name}\nSalary: {dev2.salary}\n")

dev3 = Programmer("Sahil", "15LPA")
print(f"Company Name: {dev3.company}\nDeveloper Name: {dev3.name}\nSalary: {dev3.salary}")