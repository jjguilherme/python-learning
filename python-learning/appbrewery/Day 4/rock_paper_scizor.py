import random

print("Welcome to the Rock, Paper, and Scizor game!!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scizor: "))

game = ["Rock", "Paper", "Scizor"]
random_choice = random.randint(0, 2)  # Gera um número aleatório entre 0 e 2

print(f"Computer chose: {game[random_choice]}")

if user_choice == random_choice:
    print("It's a draw!")
elif user_choice == 0 and random_choice == 2:
    print("You win! Rock beats Scizor.")
elif user_choice == 0 and random_choice == 1:
    print("You lose! Paper beats Rock.")
elif user_choice == 1 and random_choice == 2:
    print("You lose! Scizor beats Paper.")
elif user_choice == 1 and random_choice == 0:
    print("You win! Paper beats Rock.")
elif user_choice == 2 and random_choice == 0:
    print("You lose! Rock beats Scizor.")
elif user_choice == 2 and random_choice == 1:
    print("You win! Scizor beats Paper.")
