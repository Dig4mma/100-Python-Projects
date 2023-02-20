from game_data import data
from os import system, name
import random
from higher_lower_art import vs


# make a function to clear the console. cz why not :)
def clear_console():
    system('cls' if name == 'nt' else 'clear')


# 2 random dictionary are picked from the data list in game data
random_data = random.sample(data, 2)

# assign a, b
a = random_data[0]
b = random_data[1]

# printables
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
print(vs)
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

# play the game until user loose.
game = True
# keep track User's score
score = 0
while game:
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if answer is valid
    while answer != 'a' and answer != 'b':
        answer = str(input("Dude am i a joke to you? write down either 'A' or 'B': ").lower())

    # assign a/b to answer
    answer = a if answer == 'a' else b

    # results!
    max_follower = max(a['follower_count'], b['follower_count'])

    # player lose
    if max_follower != answer['follower_count']:
        clear_console()
        print(f"you lost!. your max score was {score}")
        game = False
        break
    # player wins
    else:
        score += 1
        # assign a random data to c , making sure its not equal to a, b
        c = random.choice(data)
        while c == a and c == b:
            c = random.choice(data)
        # a is assigned to b and b gets an updated value
        a, b = b, c
        clear_console()
        print(f"You're right! current score: {score}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
