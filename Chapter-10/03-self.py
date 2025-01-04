class Emlpoyee:
    language = "Python"
    salary = 2
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

data1 = Emlpoyee()
data1.name = "Aryan"
data1.language = "JavaScript"

data1.getInfo()
data1.greet()