# Blackjack Project
from blackjack_art import logo
import random

"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
"""

# https://games.washingtonpost.com/games/blackjack/

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealer_draw(deck):
    # dealer draws 2 card and anounces 1
    hand = [random.choice(cards)]
    print(f"one of the dealer's cards has {hand[0]} points.")

    # dealer keeps drawing until their hand has more than 17 points
    while sum(hand) <= 17:
        card = random.choice(cards)

        # ace handling
        if 11 in hand and card == 11:
            card = 1
        hand.append(card)
    return hand


# blackjack function
def blackjack():
    # dealer draws
    dealer = dealer_draw(cards)

    # player draws 2 random cards and ace handling
    player = random.choices(cards, k=2)
    if sum(player) == 22:
        player[1] = 1
    print(f"Your cards are: {player}, Your ponts: {sum(player)}")

    # handle instant blackjacks
    dealer_blackjack = sum(dealer[:2])
    if dealer_blackjack == 21 or sum(player) == 21:
        if dealer_blackjack == sum(player):
            return "You and Dealer are both blackjacks. DRAW!"
        elif dealer_blackjack == 21:
            return "Dealer is blackjack. YOU LOSE!"
        else:
            return f"You are blackjack. You win! \n Dealer's hand: {dealer}"

    # a silly function to draw cards and avoid ace bug
    def draw(gamer: list):
        card = random.choice(cards)
        if card == 11:
            card = 1
        gamer.append(card)
        return gamer

    # decide if player wants to hit or stand
    play = input("Type 'h' to hit, Type any key to stand. \n").lower()

    # hit
    while play == 'h' and sum(player) <= 21:
        draw(player)

        # checks if the player gets 21 score
        if sum(player) == 21:
            break

        print(f"your hand: {player}, your points: {sum(player)}")

        # checks if the player is busted
        if sum(player) > 21:
            return f"points over 21. BUSTED!\n Dealer's hand: {dealer[:2]}"


        # hit or stand?
        play = input("Type 'h' to hit, Type any key to stand. \n").lower()

    # player stands
    # player wins
    if sum(dealer) > 21 or sum(dealer) < sum(player):
        return f"Your hand: {player}, your points: {sum(player)} \n\
Dealer hand: {dealer}, dealer points: {sum(dealer)} \n\
You win!"

    # player lose
    elif sum(player) < sum(dealer):
        return f"Your hand: {player}, your points: {sum(player)} \n\
Dealer hand: {dealer}, dealer points: {sum(dealer)} \n\
You lose!"

    # draw
    else:
        return f"Your hand: {player}, your points: {sum(player)} \n\
Dealer hand: {dealer}, dealer points: {sum(dealer)} \n\
Draw!"


# a function to actually play the game
def game():
    play_game = True
    while play_game:
        print(blackjack())
        restart = input("Press 'y' if you want to play again! \n").lower()
        play_game = True if restart == 'y' else False
    print("Bye!")


game()
