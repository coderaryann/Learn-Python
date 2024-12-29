# Types of string

name = 'Aryan'
b = "Aryan"
c = """Aryan"""
d = "umbrella"

print(name[0])    # index start with 0
print(name[-1])   # length of the string -1
print(len(name))  # length of the string
print(name[0:3])  # start from index 0 all the way till 3 (excluding 3)
print(name[1:4])  # Output: rya

print(name[-4: -1])  # output is: rya
print(name[:4])  # is same as print(name[0:4]) 
print(name[1:])  # is same as print(name[1:5])

print(d[1: 7: 2])  # output is: mrl