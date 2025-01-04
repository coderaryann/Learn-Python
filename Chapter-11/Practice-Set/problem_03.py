# 3. Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrease' method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    salary = 234
    increment = 25

    @property
    def salaryAfterIncrease(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrease.setter
    def salaryAfterIncrease(self, salary):
        self.increment = ((salary/self.salary) -1) * 100

e = Employee()
salInc = (e.salaryAfterIncrease)
print(salInc)
e.salaryAfterIncrease = salInc
print(e.increment)