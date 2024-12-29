# 1. Write a program to print Twinkle twinkle little star poem in python.

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

# 2. Use REPL and print the table of 5 using it.

# Use this code in REPL

# for i in range (1, 11):
# print(f"5 * {i} = {5 * i}")

# 3. Install an external module and use it to perform an opration of your interest.

import pyttsx3
engine = pyttsx3.init()
# engine.say("I will speak this text")
engine.say("Hello, My name is Ario. nice to meet you both guys.")
engine.runAndWait()

# 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

# 5. Label the program written in problem 4 with comments.

import os

# Specify the directory path
directory_path = '/'

# Get the contents of the directory
directory_contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in directory_contents:
    print(item)
