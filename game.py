import random

options = ("paper", "rock", "scissor")
score = 0
computer_score = 0
running = True

while running:
    player = None
    computer = random.choice(options)
    
    # 1. This loop ONLY handles securing a valid user input
    while player not in options:
        player = input("choose any one (rock, scissor, paper):- ").lower().strip()
        if player not in options:
            print("Invalid choice! Please try again.")

    # 2. Reveal choices AFTER a valid input is guaranteed
    print(f"\ncomputer choice:- {computer}")
    print(f"your choice:- {player}")
    
    # 3. Game Logic (Moved safely outside the input validation loop)
    if player == "paper" and computer == "rock":
        print("congratulations! you won")
        score += 1
    elif player == "rock" and computer == "scissor":
        print("congratulations! you won")
        score += 1
    elif player == "scissor" and computer == "paper":
        print("congratulations! you won")
        score += 1
    elif computer == player:
        print("match tie")
    else:
        print("you loose\nbetter luck next time")
        computer_score += 1

    # 4. Display running scoreboard
    print(f"your score:- {score}")
    print(f"computer score:- {computer_score}\n")
    
    # 5. Safe prompt to continue or break out of the outer loop
    play_again = input("do you wanna play again (yes/no):- ").lower().strip()
    if play_again != "yes":
        running = False

print("\nThanks for playing! Final Score:")
print(f"You: {score} | Computer: {computer_score}")

