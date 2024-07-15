#rock paper scissors game
import random

print("\n***** Welcome to the Rock-Paper-Scissors game! *****\n")

p1_cs = 0
p2_us = 0
a = input("Enter your name: ")
rounds = int(input("Enter the number of rounds for the game: "))
r = 1
it = []

while r <= rounds:
    choice = int(input("\nEnter 0 for stone, 1 for paper, or 2 for scissors: "))
    cv = random.randint(0, 2)

    if cv == choice:
        it.append(f"Round {r} - It's a tie")
        print(f"You entered {choice}, computer played {cv}, result: It's a tie")
    elif (cv == 0 and choice == 1) or (cv == 1 and choice == 2) or (cv == 2 and choice == 0):
        it.append(f"Round {r} - {a} wins")
        p2_us += 1
        print(f"You entered {choice}, computer played {cv}, result: {a} wins")
    else:
        it.append(f"Round {r} - Computer wins")
        p1_cs += 1
        print(f"You entered {choice}, computer played {cv}, result: Computer wins")

    r += 1

print("\nComputer score:", p1_cs)
print(f"{a} score:", p2_us)
print("Number of rounds played:", r - 1)

for item in it:
    print(item)

if p2_us > p1_cs:
    print(f"{a} wins the game!")
elif p2_us == p1_cs:
    print("Oops, this game ties. Try again!")
else:
    print("Computer wins the game! Better luck next time.")
