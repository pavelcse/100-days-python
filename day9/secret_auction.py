import os
print("Welcome to Secret Auction")
from art import logo
print(logo)

is_auction_closed = False
bidders = {}

def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for biddle in bidding_records:
        bid_amount = bidding_records[biddle]
        
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = biddle
    print(f"The winner is {winner} and the bid amount is {highest_bid}")
           
    
while not is_auction_closed:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    is_bid_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    bidders[name] = bid
    
    if is_bid_continue == "no":
        is_auction_closed = True
        find_highest_bidder(bidders)
    else:
        os.system("cls")

