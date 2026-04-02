import random
import time

# Game choices
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock Paper Scissors Game!")
print("🔥 First to 5 points wins the game!\n")

# Game loop
while True:
    # User input
    user = input("👉 Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user == "exit":
        print("👋 Thanks for playing!")
        break

    if user not in choices:
        print("❌ Invalid input! Try again.\n")
        continue

    # Computer choice
    computer = random.choice(choices)

    # Countdown
    print("\n⏳ Get ready...")
    for word in ["Rock...", "Paper...", "Scissors...", "Shoot! ✊✋✌️"]:
        print(word)
        time.sleep(0.6)

    # Show choices
    print(f"\n🧑 You chose: {user}")
    print(f"💻 Computer chose: {computer}")

    # Game logic
    if user == computer:
        print("🤝 It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win this round!")
        user_score += 1

    else:
        print("💻 Computer Wins this round!")
        computer_score += 1

    # Display scores
    print(f"\n📊 Score → You: {user_score} | Computer: {computer_score}\n")

    # Check winner
    if user_score == 5:
        print("🏆 Congratulations! You won the game! 🎉")
        break
    elif computer_score == 5:
        print("💻 Computer wins the game! Better luck next time 😄")
        break
