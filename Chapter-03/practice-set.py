# 01. Write a python program to display a user entered name followed by Good Afternoon using input() function.
print("Q. no. 1 solution.")

user_name = input("Enter your name: ")
print(f"Good morning, {user_name}")

# 02. Write a program to fill in a letter template given below with name and date.
print("Q. no. 2 solution.")

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>", "Aryan").replace("<|Date|>", "29 Dec 2024"))

# 03. Write a program to detect double space in a string.
print("Q. no. 3 solution.")

double_spc = "This is my book  and  those are your pens."
print(double_spc.find("  "))
print(double_spc.count("  "))

# 04. Replace the double space from problem 3 with single spaces.
print("Q. no. 4 solution.")

print(double_spc)
print(double_spc.replace("  ", " "))
print(double_spc)  # Strings are immutable which means that you cannot change them by running functions on them!

# 05. Write a program to format the following letter using escape sequence characters.
print("Q. no. 5 solution.")

letter = "Dear Aryan,\nthis python course is nice.\nThanks!"
print(letter)