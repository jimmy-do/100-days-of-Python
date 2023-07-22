from art import logo

print(logo)

auction_log = []
bidding_finished = False


def add_name_and_bid(bidder, bid_price):
    dictionary = {'name': bidder, 'bid': bid_price}
    auction_log.append(dictionary)


def find_highest_bidder():
    for bidder in auction_log:
        highest_bidder = 0
        winner = ""
        if int(bidder['bid']) > highest_bidder:
            highest_bidder = bidder['bid']
            winner = bidder['name']
    print(f'{winner} has the highest bid with {highest_bidder}!')


while not bidding_finished:
    name = input('Please enter in your name: ')
    bid = int(input('Please enter in your bid price: '))
    add_name_and_bid(name, bid)
    should_continue = input('Are there any other bidders? Y or N?').lower()
    if should_continue == 'n':
        find_highest_bidder()
        bidding_finished = True
    elif should_continue == 'y':
        continue
