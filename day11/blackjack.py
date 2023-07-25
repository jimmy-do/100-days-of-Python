import random

game_over = False
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
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score


print(calculate_score(computer_hand))
print(calculate_score(user_hand))

comp_score = calculate_score(computer_hand)
user_score = calculate_score(user_hand)

if comp_score == 0 or user_score == 0 or user_score >= 21:
    game_over = True
while not game_over:
    if user_score > 21:
        print('Computer has won. AI world dominion is imminent.')
        exit(0)
    hit_or_stay = input('Do you want to hit or stay? ').lower()
    if hit_or_stay == 'hit' and user_score < 21:
        user_hand.append(deal_card(cards))
        user_score = calculate_score(user_hand)
        print(user_score)
    elif hit_or_stay == 'stay':
        break
    else:
        game_over = True

while calculate_score(computer_hand) < 17:
    computer_hand.append(deal_card(cards))
    print(calculate_score(computer_hand))
    if comp_score > 21:
        print('Humanity prevails. We live to fight another day.')
        break


def compare(computer, user):
    if computer > user:
        print('Computer has won. AI world dominion is imminent.')
    elif user < computer:
        print('Humanity prevails. We live to fight another day.')
    else:
        print('Draw')


compare(comp_score, user_score)
