# Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from number_guessing_art import logo

print(logo)
# a function to make players choose difficulty instead of bullshit and return the number of lives the player has in each difficulty
def difficulty_checker():
    difficulty = input("Welcome to the number guessing game! \n im thinking of a number between 1 and 100. \n choose a difficulty. type 'easy' or 'hard' \n").lower()

    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("are you fucking with me? simply type 'easy' or 'hard' \n ").lower()

    life = 10 if difficulty == 'easy' else 5
    print(f"you have {life} lives because you chose {difficulty} mode.")
    return life


# the actual game:
def number_gussing():

    # 1- choose difficulty and get lives value
    lives = difficulty_checker()

    # 2- guess a random number between 1 and 100
    random_number = int(random.randint(1, 100))

    # 3- player is asked to guess a number while they are not out of lives
    while lives > 0:

        # player may fuck around the game and use other types instead of int.
        while True:
            try:
                guessed_number = int(input("guess your number: "))
                break
            except ValueError:
                print("if you dont know what a number means, you can ask your MOM!")

        # player guessed right
        if guessed_number == random_number:
            print(f"you guessed right! the answer is {guessed_number}")
            return "winner"

        # player guessed wrong
        else:
            # reduce lives point by 1
            lives -= 1
            print("you guessed high") if guessed_number > random_number else print("you guessed low")
            print(f"you have {lives} lives left.")

    # exit the round
    print(f"you have failed to guess {random_number}. your luck sucks!")
    return "loser"


def game():
    play = True
    while play:
        number_gussing()
        play = input("press 'q' to quit playing, press any other keys play again: ").lower()
        if play == 'q':
            play = False
            print("bye! Try harder next time!")
        else:
            play = True


game()
