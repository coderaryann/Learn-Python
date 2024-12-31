# 01. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
print("Q. no. 1 solution")
words = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

# 02. Write a program to input eight numbers from the user and display all the unique numbers (once).
print("Q. no. 2 solution")

s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
print(s)

# 03. Can we have a set with 18 (int) and "18" (str) as a value in it?
print("Q. no. 3 solution")

s = set()
s.add(18)
s.add("18")
print(s)

# 04. What will be the length of following set S:
# s = Set(), s.add(20), s.add(20.0), s.add('20')
# length of s after these operations?
print("Q. no. 4 solution")

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s), s)

# 05. S = {}, What is the type of S?
print("Q. no. 5 solution")

s = {}
print(type(s))

# 06. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
print("Q. no. 6 solution")

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)

# 07. If the names of 2 friends are same; what will happen to the program in problem 6?
print("Q. no. 7 solution")

# Run the program 6 and check

# 08. If languages of two freinds are same; what will happen to the program in problem 6?
print("Q. no. 8 solution")

# Run the program 6 and check

# 09. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Aryan", [1, 2]}
print("Q. no. 9 solution")

s = {8, 7, 12, "Aryan", [1, 2]}

# s[4][0] = 9  # I cannot do this Circus!