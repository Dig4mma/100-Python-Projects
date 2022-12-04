import random

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
          ''', '''
    +---+
     |   |
     O   |
    /|\  |
         |
         |
 =========
     ''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
 =========
               ''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
 =========
          ''', '''
     +---+
     |   |
     O   |
         |
         |
         |
 =========
            ''', '''
     +---+
     |   |
         |
         |
         |
         |
 =========
               ''']

word_list = ["ardvark", "baboon", "camel", "bigmac", "axe", "cannabis", "mushrooms"]
chosen_word = random.choice(word_list)
lives = 7

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in chosen_word:
    display.append("_")

print(f"{' '.join(display)}")
while lives > 0 and "_" in display:
    guess = input("Guess the letter! \n").lower()
    if guess not in chosen_word:
        lives -= 1
        print(f"You lost a live! You have {lives} lives left!")
        print(stages[lives])
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    print(f"{' '.join(display)}")


if lives > 0:
    print("You won!")
else:
    print("Game Over!")
    print(stages[0])
