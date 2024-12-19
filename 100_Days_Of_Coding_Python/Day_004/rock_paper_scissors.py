# sourcery skip: assign-if-exp, merge-duplicate-blocks, remove-redundant-if, switch
import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
pc_choice = r.randint(0,2)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

result = 0
if player_choice == 0:
    if pc_choice == 0:
        result = 0
    elif pc_choice == 1:
        result = 1
    else:
        result = 2

if player_choice == 1:
    if pc_choice == 1:
        result = 0
    elif pc_choice == 0:
        result = 1
    else:
        result = 2

if player_choice == 2:
    if pc_choice == 2:
        result = 0
    elif pc_choice == 1:
        result = 1
    else:
        result = 0

print(rps[player_choice])
print("Computer Choice:")
print(rps[pc_choice])

if result == 0:
    print("It's a draw.")
elif result == 1:
    print("You won!")
else:
    print("You lost.")
