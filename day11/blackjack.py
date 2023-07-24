import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    deal = random.choice(deck)
    return deal


computer_hand = []
user_hand = []

computer_hand.append(deal_card(cards))
user_hand.append(deal_card(cards))
computer_hand.append(deal_card(cards))
user_hand.append(deal_card(cards))


def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        print('Blackjack!')
        return 0
    elif score > 21:
        hand = hand.remove[11]
        hand.append(1)
        score = sum(hand)
        return score
    else:
        return score


print(calculate_score(computer_hand))
print(calculate_score(user_hand))
