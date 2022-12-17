from secret_auction_art import logo
from os import system
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program!")
auction = {}
finish = "yes"

while finish == 'yes':
    name = input("What is your name?\n").lower()
    bid = int(input("What's your bid?\n"))
    auction[name] = bid
    finish = input("Are there any other bidders? Type 'yes' if so. press any key if not. \n").lower()
    system('cls||clear')

winner_bid = max(auction.values())
winner_name = ''
for key, val in auction.items():
    if val == winner_bid:
        winner_name = key

print(logo)
print(f"The winner is {winner_name} with a bid of {winner_bid}")