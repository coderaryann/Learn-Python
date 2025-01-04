class Employee:
    def __init__(self):
        print("Constructor of Employee")

    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder(Employee):
    def __init__(self):
        print("Constructor of Coder")

    language = "Python"
    def PrintLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Coder):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")

    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

b = Programmer()
c = Employee()
d = Coder()