import random

choices = ["Rock", "Paper", "Scissors"]

print("====== ROCK PAPER SCISSORS GAME ======")

while True:
    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("Enter your choice (1-4): ")

    if user_choice == "4":
        print("Thank You for Playing!")
        break

    if user_choice not in ["1", "2", "3"]:
        print("Invalid Choice! Please try again.")
        continue

    user_choice = int(user_choice)
    user = choices[user_choice - 1]
    computer = random.choice(choices)

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        print("🎉 Congratulations! You Win!")

    else:
        print("💻 Computer Wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank You for Playing!")
        break