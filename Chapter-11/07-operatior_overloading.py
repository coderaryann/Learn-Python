class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):  # __add__ for adding
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)

# a + b __add__ for addition
# a - b __sub__ for substract
# a * b __mul__ for multiply
# a / b __truediv__ for divide
# a // b __floordiv__ for divide