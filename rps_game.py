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

tie = "Tie!"
win = "You win!"
lose = "You lose!"

#Write your code below this line 👇

user_choice = input("Type 0 for Rock, 1 for Paper, or 2 for scissors")

user_choice = int(user_choice)

computer_choice = random.randint(0,2)

print(user_choice, computer_choice)

# Handle Ties
if user_choice == 0 and computer_choice == 0:
    print(tie)
if user_choice == 1 and computer_choice == 1:
    print(tie)
if user_choice == 2 and computer_choice == 2:
    print(tie)

#Handle User Wins
if user_choice == 0 and computer_choice == 2:
    print(win)
if user_choice == 1 and computer_choice == 0:
    print(win)
if user_choice == 2 and computer_choice == 1:
    print(win)

#Handle User Loses
if user_choice == 0 and computer_choice == 1:
    print(lose)
if user_choice == 1 and computer_choice == 2:
    print(lose)
if user_choice == 2 and computer_choice == 0:
    print(lose)
