from replit import clear
from art import logo

print(logo)

bids = {}

keep_going = "yes"
while (keep_going == "yes"):
    
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    
    bids[name] = bid
    
    keep_going = input('Are there any other bidders? Type "yes" or "no".\n').lower()
    
    clear()

highest_bid = 0
highest_bidder = ""
for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")