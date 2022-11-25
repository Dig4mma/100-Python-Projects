print('''
*******************************************************************************
|                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
|                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
|           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. where do you want to go? type 'left' or 'right'.\n")
if direction != "left":
    print("You fell into a hole! Game Over!")
else:
    island = input("You came to a lake. there is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if island != "wait":
        print("You have been attacked by a trout! Game Over!")
    else:
        color = input("You arrived at the island unharmed. There is a house within 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if color == "blue":
            print("You have been eaten by beasts! Game Over!")
        elif color == "red":
            print("You have burnt by fire! Game Over!")
        elif color == "yellow":
            print("You Won!")
        else:
            print("are you trying to cheat? Game Over!")
