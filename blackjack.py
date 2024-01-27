from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_playing = True

alive = True
game_over = False


def starting_game():
    global player_cards
    player_cards = []
    global dealer_cards
    dealer_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    print(f"{player_cards} Your total: {sum(player_cards)}")
    print(f"{dealer_cards} Dealer total: {sum(dealer_cards)}")


while continue_playing:
    os.system('cls')
    print(logo)
    starting_game()
    while alive:
        choice = input("Press 'y' if you want another card, else press 'n'. ")
        if choice == 'y':
            player_cards.append(random.choice(cards))
            print(f"{player_cards} Your total: {sum(player_cards)}")
            if sum(player_cards) > 21:
                game_over = True
                alive = False
                print("You lost :(")
        elif choice == 'n':
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.choice(cards))
                print(f"{dealer_cards} Dealer total: {sum(dealer_cards)}")
                if 17 <= sum(dealer_cards) <= 21:
                    alive = False
                elif sum(dealer_cards) > 21:
                    alive = False
                    game_over = True
                    print("You won :)")
    if not game_over:
        if sum(player_cards) > sum(dealer_cards):
            print("You won :)")
        elif sum(player_cards) == sum(dealer_cards):
            print("Tie :/")
        elif sum(player_cards) < sum(dealer_cards):
            print("You lost :(")

    alive = True
    game_over = False

    if input("Do you want to play another game? Press 'y' if yes and 'n' if no. ") == 'n':
        continue_playing = False
