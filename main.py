import random
from resource import logo, cards


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(cards_in_hand):
    if sum(cards_in_hand) == 21 and len(cards_in_hand) == 2:
        return 0

    if 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)

    return sum(cards_in_hand)


def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over 21. You lose!"
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose! Opponent has blackjack."
    elif user_score == 0:
        return "You Win! You have blackjack."
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "You win!. Opponent went over 21."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def start_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for temp in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to start game? Type 'Y' or 'N': ").lower() == "y":
    start_game()

