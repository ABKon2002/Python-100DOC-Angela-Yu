from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to today's secret auction.")
bids = {}

def add_bid(name, bid):
    bids[name] = bid

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bid(name, bid)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        clear()
