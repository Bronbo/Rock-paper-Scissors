#Rock Paper Scissors project October 20th
import random
print("Hello, welcome to a game of Rock Paper Scissors! You must answer the following prompt by typing Rock, Paper, or Scissors")
replay = True
while replay == True:
    Response = input("Choose Rock, Paper, or Scissors: ")
    Response = Response.lower()
    ai_choice = random.randint(1, 3)
    if Response == "rock":
        if ai_choice == 2:
            print("You lost! The computer has choosen Paper!")
        if ai_choice == 3:
            print("You won! The computer has choosen Scissors!")
        if ai_choice == 1:
            print("You tied! The computer has also choosen Rock!")
    if Response == "paper":
        if ai_choice == 1:
            print("You won! The computer has choosen Rock!")
        if ai_choice == 3:
            print("You lost! The computer has choosen Scissors!")
        if ai_choice == 2:
            print("You tied! The computer has also choosen Paper!")
    if Response == "scissors":
        if ai_choice == 1:
            print("You lost! The computer has choosen Rock!")
        if ai_choice == 2:
            print("You won! The computer has choosen Paper!")
        if ai_choice == 3:
            print("You tied! The computer has also choosen Scissors!")
    replay = input("Do you want to play again? Type Yes or No: ")
    replay = replay.lower()
    if replay != "yes":
        replay = False
    else: 
        replay = True

