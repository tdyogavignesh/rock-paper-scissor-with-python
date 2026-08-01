import random
options =   ("paper","rock","scissor")
player = None
score = 0
computer_score = 0
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("choose any one(rock,scissor,paper):- ")
        print(f"computer choice:- {computer}")
        print(f"your choice:- {player}")
        if player == "paper" and computer == "rock":
            print("congratulations! you won")
            score += 1
            print(F"your score:- {score}")
            print(F"computer score:- {computer_score}")
            play_again = input("do you wanna play again (yes/no):- ")
            if not play_again == "yes":
                 running = False
        elif player == "rock" and computer =="scissor":
            print("congratulations! you won")
            score += 1
            print(f"your score:- {score}")
            print(f"computer score:-{computer_score}")
            play_again = input("do you wanna play again (yes/no):- ")
            if not play_again == "yes":
                 running = False
        elif computer == player:
            print("match  tie")
            play_again = input("do you wanna play again (yes/no):- ")
            if not play_again == "yes":
                 running = False
        elif player == "scissor" and computer == "paper":
            print("congratulations! you won")
            score += 1
            print(f"your score:- {score}")
            print(f"computer score:-{computer_score}")
            play_again = input("do you wanna play again (yes/no):- ")
            if not play_again == "yes":
                 running = False
        else:
            print("you loose\nbetter luck next time")
            computer_score += 1
            print(f"your score:- {score}")
            print(f"computer score:- {computer_score}")
            play_again = input("do you wanna play again (yes/no):- ")
            if not play_again == "yes":
              running = False    
