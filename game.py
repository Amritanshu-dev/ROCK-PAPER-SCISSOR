"""
Rock-Paper-Scissors Game ✂️📄🪨
-------------------------------
You play against the computer in the classic Rock–Paper–Scissors match.

Features:
- Score tracking (Player vs Computer)
- High score tracking (fewest rounds needed to beat the computer)
- Multiple rounds until you choose to quit
- Replay option
- Fair computer moves (randomized)

How to Play:
1. Choose Rock, Paper, or Scissors by typing your choice (or short form r/p/s).
2. Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
3. First to win more rounds is the champion!
"""

import random

def rock_paper_scissors():
    high_score = None  # fewest rounds player needed to win

    while True:
        player_score = 0
        computer_score = 0
        rounds_played = 0

        print("\n🎮 Game Started: Rock-Paper-Scissors!")
        print("Type 'rock', 'paper', or 'scissors' (or r/p/s). Type 'quit' to stop.\n")

        while True:
            player_choice = input("👉 Enter your choice: ").lower()
            if player_choice in ["quit", "q"]:
                break

            # allow short forms
            if player_choice == "r":
                player_choice = "rock"
            elif player_choice == "p":
                player_choice = "paper"
            elif player_choice == "s":
                player_choice = "scissors"

            if player_choice not in ["rock", "paper", "scissors"]:
                print("⚠️ Invalid choice. Please choose rock, paper, or scissors.")
                continue

            computer_choice = random.choice(["rock", "paper", "scissors"])
            rounds_played += 1

            print(f"🧑 You chose: {player_choice}")
            print(f"💻 Computer chose: {computer_choice}")

            # Determine winner
            if player_choice == computer_choice:
                print("🤝 It's a tie!")
            elif (
                (player_choice == "rock" and computer_choice == "scissors") or
                (player_choice == "scissors" and computer_choice == "paper") or
                (player_choice == "paper" and computer_choice == "rock")
            ):
                print("✅ You win this round!")
                player_score += 1
            else:
                print("❌ Computer wins this round!")
                computer_score += 1

            # Show current score
            print(f"📊 Score => You: {player_score} | Computer: {computer_score}\n")

        # End of one game session
        print("\n🏁 Game Over!")
        print(f"Final Score => You: {player_score} | Computer: {computer_score}")
        
        if player_score > computer_score:
            print("🎉 Congratulations, you WON the game!")
            # High score: track the least rounds needed for a win
            if high_score is None or rounds_played < high_score:
                high_score = rounds_played
                print("🏆 New High Score (least rounds needed to win)!")
        elif player_score < computer_score:
            print("😢 Computer WON the game!")
        else:
            print("🤝 It's a DRAW!")

        # Show high score if exists
        if high_score:
            print(f"📊 Current High Score: Won in {high_score} rounds")

        # Replay option
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing Rock-Paper-Scissors! Goodbye.")
            break

# Run the game
rock_paper_scissors()
