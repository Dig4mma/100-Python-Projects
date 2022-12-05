import random
import hangman_arts
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
lives = 7
print(hangman_arts.logo)
stages = hangman_arts.stages

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
        print(f"{guess} is not in the word.")
        print(f"You lost a live! You have {lives} lives left!")
        print(stages[lives])
    elif guess in display:
        print(f"You already guessed {guess}")
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
