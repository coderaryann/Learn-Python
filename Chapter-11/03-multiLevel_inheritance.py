class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder(Employee):
    language = "Python"
    def PrintLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

b = Programmer()
b.show()
b.PrintLanguages()
b.showLanguage()