# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is equal to {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n} is equal to {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The square root of {self.n} is equal to {round(self.n**1/2)}")

    @staticmethod
    def hello():
        print("Hello there!")

cal = Calculator(4)
cal.hello()
cal.square()
cal.cube()
cal.squareRoot()