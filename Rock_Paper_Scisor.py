import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Please type a valid option.")
        continue

    numbers = random.randint(0, 2)
    computer_input = options[numbers]
    print("computer picked ", computer_input)

    if user_input == "rock" and computer_input == "scissors":
        if user_input == "rock" and computer_input == "rock":
            print("a tie has occurred")
            continue
        print("You won")
        user_wins +=1

    elif user_input == "paper" and computer_input == "rock":
        if user_input == "paper" and computer_input == "paper":
            print("a tie has occurred")
            continue
        print("You won")
        user_wins +=1

    elif user_input == "scissors" and computer_input == "paper":
        if user_input == "scissors" and computer_input == "scissor":
            print("a tie has occurred")
            continue
        print("You won")
        user_wins +=1

    else:
        print("You lost")
        computer_wins +=1


print(f"User won {user_wins} times.")
print(f"Coputer won {computer_wins} times.")
print("Goodbye")