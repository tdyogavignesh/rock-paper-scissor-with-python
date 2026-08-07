import random

options = ("rock", "paper", "scissor")

player_score = 0
computer_score = 0
round_no = 1
running = True

# Dictionary that stores which choice beats which
wins = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}

while running:
    print(f"\n========== Round {round_no} ==========")

    computer = random.choice(options)
    player = None

    # Get valid input
    while player not in options:
        player = input("Choose (rock, paper, scissor): ").lower().strip()

        if player not in options:
            print("❌ Invalid choice! Try again.")

    print(f"\nYour Choice     : {player}")
    print(f"Computer Choice : {computer}")

    # Decide winner
    if player == computer:
        print("🤝 It's a Tie!")
    elif wins[player] == computer:
        print("🎉 You Won!")
        player_score += 1
    else:
        print("💻 Computer Won!")
        computer_score += 1

    # Scoreboard
    print("\n------ Scoreboard ------")
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")

    play_again = input("\nPlay again? (yes/no): ").lower().strip()

    if play_again != "yes":
        running = False

    round_no += 1

print("\n========== GAME OVER ==========")
print(f"Final Score")
print(f"You      : {player_score}")
print(f"Computer : {computer_score}")

if player_score > computer_score:
    print("🏆 Congratulations! You are the overall winner!")
elif computer_score > player_score:
    print("😔 Computer wins the game!")
else:
    print("🤝 The game ended in a tie!")

print("Thanks for playing!")
