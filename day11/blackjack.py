import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    deal = random.choice(deck)
    return deal


computer_hand = []
user_hand = []

computer_hand.append(deal_card())