import random

print("Snake, Water, Gun Game")
computer = random.choice([0, -1, 1])
youstr = input("Enter s, w or g: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]


print(f"Computer = {reverseDict[computer]} & You = {reverseDict[you]}")

if (computer == you):
    print("Tie")

else:
    # if (computer == -1 and you == 1): # (computer - you) logic  # (-1 -1) = -2
    #     print("You win!")

    # elif (computer == -1 and you == 0):    # (-1 -0) = -1
    #     print("You lose!")

    # elif (computer == 1 and you == -1):    # (1 -(-1)) = 2
    #     print("You lose!")

    # elif (computer == 1 and you == 0):    # (1 -0) = 1
    #     print("You win!")

    # elif (computer == 0 and you == 1):    # (0 -1) = -1
    #     print("You lose!")

    # elif (computer == 0 and you == -1):    #(0 -(-1)) = 1
    #     print("You win!")


    # (computer - you) logic
    if ( (computer - you) == -1 or (computer - you) == 2 ):
        print("You lose!")

    elif ( (computer - you) == 1 or (computer - you) == -2):
        print("You win!")
    

print("Run Again!")