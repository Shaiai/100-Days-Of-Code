import random

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

#Write your code below this line 👇

print("Welcome to the professional rock paper scissors league!")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))

bot_choice = random.randint(0,2)

if player_choice == 0 and bot_choice == 0:
    print(f'{rock}\nComputer chose:\n{rock}\nIt\'s a draw!')
elif player_choice == 0 and bot_choice == 1:
    print(f'{rock}\nComputer chose:\n{paper}\nYou lose!')
elif player_choice == 0 and bot_choice == 2:
    print(f'{rock}\nComputer chose:\n{scissors}\nYOU WIN!')

if player_choice == 1 and bot_choice == 0:
    print(f'{paper}\nComputer chose:{rock}\nYOU WIN')
elif player_choice == 1 and bot_choice == 1:
    print(f'{paper}\nComputer chose\n{paper}\nIt\'s a DRAW')
elif player_choice == 1 and bot_choice == 2:
    print(f'{paper}\nComputer chose:\n{scissors}\nYOU LOSE! LOSER!')

if player_choice == 2 and bot_choice == 0:
    print(f'{scissors}\nComputer chose:{rock}\nYou lose! Like always')
if player_choice == 2 and bot_choice == 1:
    print(f'{scissors}\nComputer chose:{paper}\nYou win for once!')
if player_choice == 2 and bot_choice == 2:
    print(f'{scissors}\nComputer chose:{scissors}\nIt\'s a draw!')
