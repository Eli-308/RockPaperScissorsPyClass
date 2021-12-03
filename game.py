import random

print("Rock Paper Scissors")
print("Enter 'R' for Rock, 'P' for Paper and 'S' for Scissors")

response = input("Enter your move: ")

aiResponse = random.random(0, 2)

if response == "R":
    if aiResponse == 0:
        print("Rock!")
        print("Its a tie")
    elif aiResponse == 1:
        print("Paper")
        print("I win!")
    elif aiResponse == 2:
        print("Scissors!")
        print("You win!")

if response == "P":
    if aiResponse == 0:
        print("Rock!")
        print("You win!")
    elif aiResponse == 1:
        print("Paper")
        print("Its a tie")
    elif aiResponse == 2:
        print("Scissors!")
        print("I win!")

if response == "S":
    if aiResponse == 0:
        print("Rock!")
        print("I win!")
    elif aiResponse == 1:
        print("Paper")
        print("You win!")
    elif aiResponse == 2:
        print("Scissors!")
        print("Its a tie")