import random

# 🎲 Dice roll function
# 👉 6 dice ni roll chesi results list lo return chestundi
def roll_dice():
    six_dices_result = []
    for _ in range(0, 6):
        random_number = random.randint(1, 6)
        six_dices_result.append(random_number)
    return six_dices_result


# 💰 Starting balance input
# 👉 Player daggara unna amount teesukuntundi
balance = int(input("\nEnter your balance amount 💰: "))


# 🔁 Game loop (balance unna varaku aaduthundi)
while balance > 0:
    try:
        # Kai Rajaa Kaii..
        print("\n🔥 Let's Play - Dice Betting Game 🔥")

        # 💸 Bet amount input
        # 👉 Player entha bet pettalo adugutundi
        bet = int(input("Enter bet amount 💵: "))

        # ❌ Bet ekkuva unte reject chestundi
        # 👉 Balance kanna ekkuva bet pettakudadhu
        if bet > balance:
            print("⚠️ Not enough balance! Bet within your limit.")
            continue

        # 🎯 Number selection
        # 👉 Player 1 nundi 6 madhya number select chestadu
        choice = int(input("Choose a number (1-6) 🎯: "))

        # ❌ Invalid number check
        if choice < 1 or choice > 6:
            print("❌ Invalid number! Choose between 1 and 6.")
            continue

        # 🎲 Dice rolling
        # 👉 6 dice results generate chestundi
        dices = roll_dice()
        print("🎲 Rolling dice... Results:", dices)

        # 🔢 Count chosen number occurrences
        # 👉 Player select chesina number entha sarlu vachindo count chestundi
        count = dices.count(choice)

        # 🏆 Winning condition
        # 👉 Minimum 2 times vaste win
        if count >= 2:
            win_amount = bet * count
            balance += win_amount
            print(f"🎉 Your number appeared {count} times! You won ₹{win_amount}")
        else:
            # 😢 Losing condition
            balance -= bet
            print("😢 Your number did not appear enough times. You lost!")

        # 💰 Balance update
        print("💰 Current Balance:", balance)

        # 🔄 Play again option
        # 👉 Player malli aadala ani adugutundi
        play = input("Do you want to play again? (y/n): ").lower()
        if play != 'y':
            break

    except ValueError:
        # ❌ Invalid input handling
        print("❌ Please enter valid numbers only!")

# 🏁 Game end
print("\n🏁 Game Over! Final Balance:", balance)
