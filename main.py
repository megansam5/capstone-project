import random

ranks_as_numbers = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


def choose_cards():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
    chosen_cards = []
    while len(chosen_cards) < 6:
        rank = random.choices(ranks)
        suit = random.choices(suits)
        if [rank[0], suit[0]] not in chosen_cards:
            chosen_cards.append([rank[0], suit[0]])
    return chosen_cards


def calculate_number(rank):

    try:
        result = int(rank)
    except:
        result = ranks_as_numbers[rank]

    return result


def play_game():
    cards = choose_cards()
    print(f'Your first card is {cards[0][0]} of {cards[0][1]}.')

    for i in range(len(cards) - 2):
        guess = input("Will the next card be higher (h) or lower (l)? ")
        current = calculate_number(cards[i][0])
        next = calculate_number(cards[i+1][0])
        print(f'The next card is {cards[i+1][0]} of {cards[i+1][1]}.')
        if guess == 'h' and next > current:
            print('You guessed higher correctly!')
        elif guess == 'l' and next < current:
            print("You guessed lower correctly!")
        elif next == current:
            print("They are the same so we'll give it to you as correct!")
        else:
            print('Unlucky!')


play_game()
