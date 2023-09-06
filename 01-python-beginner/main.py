import random
from art import logo, vs
from game_data import data

# pycharm cannot run this function
from replit import clear


def choose(compare):
    """Format the account data into printable format."""
    name = compare["name"]
    description = compare["description"]
    country = compare["country"]
    return f"{name}, a {description}, from {country}"


def game():
    score = 0
    answer = 0
    is_continue = True
    print(logo)
    print("")
    compare_b = random.choice(data)

    while is_continue:
        compare_a = compare_b
        compare_b = random.choice(data)
        if compare_a == compare_b:
            compare_b = random.choice(data)

        print(f"Compare A: {choose(compare_a)}")
        print(vs)

        print(f"Against B: {choose(compare_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if compare_a["follower_count"] < compare_b["follower_count"]:
            answer = "B"
        else:
            answer = "A"

        # pycharm cannot run this function
        clear()

        print(logo)

        if guess == answer:
            score += 1
            # print(logo)
            print(f"You're right, current score: {score}. ")

        else:
            # print(logo)
            print(f"You're wrong, current score: {score}.")
            is_continue = False


game()
