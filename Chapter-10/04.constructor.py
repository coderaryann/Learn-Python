class Emlpoyee:
    language = "Python"
    salary = 2
    
    def __init__(self, name, salary, language):  # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = salary
        print("I'm creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

data1 = Emlpoyee("Aryan", 5, "JavaScript")
# data1.name = "Aryan"
print(data1.name, data1.salary)