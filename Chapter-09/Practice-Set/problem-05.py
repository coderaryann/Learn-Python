# 5. Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "bad", "lie"]

with open ("./Learn-Python/Chapter-09/Practice-Set/05-prob.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open ("./Learn-Python/Chapter-09/Practice-Set/05-prob.txt", "w") as f:
    f.write(content)