# import random
from random import randint

# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make your move: ").lower()
# rand_num = random.randint(0, 2)
rand_num = randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    # elif computer == "paper":
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    # elif computer == "scissors":
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    # elif computer == "rock":
    else:
        print("computer wins!")
else:
    print("something went wrong")