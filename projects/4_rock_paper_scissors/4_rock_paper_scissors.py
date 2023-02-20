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

middle = '''
    _______
---'   ____)
      (____)____
       _________)
      (____)
---.__(___)
'''

slot = [rock, paper, scissors]
ai = random.randint(0, len(slot) - 1)
choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))


if choice in range(3):
    print(slot[choice])
    print("Computer chose:" + (slot[ai]))
else:
    print("You've chosen a wrong number! YOU LOSE!")
    print(middle)


if choice == ai:
    print("Draw!")
else:
    if choice == 0 and ai == 1:
        print("You Lose!")
    elif choice == 0 and ai == 2:
        print("You Win!")
    elif choice == 1 and ai ==0:
        print("You Win!")
    elif choice == 1 and ai == 2:
        print("You Lose!")
    elif choice  == 2 and ai == 0:
        print("You Lose!")
    elif choice == 2 and ai == 1:
        print("You Win!")
