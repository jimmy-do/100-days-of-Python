from art import logo, vs
from game_data import data
import random

score = 0


def check_answer(a, b, ans):
    global score
    a_follower_count = data[a]['follower_count']
    b_follower_count = data[b]['follower_count']

    if ans == 'a' and a_follower_count > b_follower_count:
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    elif ans == 'b' and a_follower_count < b_follower_count:
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    else:
        exit(f"You're wrong. Final score: {score}")


def play_game():
    INFLUENCER_1 = random.randint(0, len(data))
    INFLUENCER_2 = random.randint(0, len(data))
    print(
        f"Compare A: {data[INFLUENCER_1]['name']} a {data[INFLUENCER_1]['description']} from {data[INFLUENCER_1]['country']}.")
    print(vs)
    print(
        f"Compare B: {data[INFLUENCER_2]['name']} a {data[INFLUENCER_2]['description']} from {data[INFLUENCER_2]['country']}.")
    user_answer = input("Who has more followers? Type 'A' or 'B'").lower()
    check_answer(INFLUENCER_1, INFLUENCER_2, user_answer)


while True:
    play_game()
