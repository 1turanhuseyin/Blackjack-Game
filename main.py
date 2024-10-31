import random
from art import logo

choice = input("Do you want to play a game of Blackjack? Type (Y)es or (N)o:  ").lower()

bank = 1000

while choice == "y":
    print(f"\n" * 42)
    print(logo)
    print(f"Bank: ${bank}\n")
    print(" \t $10 \t $20 \t $50 \t $100 \t $500 \t ")
    bet_amount = int(input("How much would you like to bet? \t $"))
    print()
    while bet_amount > bank or bet_amount % 10 != 0:
        if bet_amount > bank:
            print("There is not enough money in the bank. Please enter a lower bet amount...")

        if bet_amount % 10 != 0:
            print("Please enter a number that is a multiple of 10...")

        bet_amount = int(input("How much would you like to bet? \t $"))
        print()


    def deal_cards():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random.shuffle(cards)
        card = random.choice(cards)
        return card


    def calculate_score(cards):
        if sum(cards) > 21 and 11 in cards:
            card_eleven_index = cards.index(11)
            cards[card_eleven_index] = 1
            return sum(cards)
        else:
            return sum(cards)

    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    player_total = calculate_score(player_cards)
    computer_total = calculate_score(computer_cards)

    if computer_total == 21:
        print("Computer's hand is 21 BLACKJACK !")
    elif player_total == 21:
        print("Your hand is 21 BLACKJACK !")
    else:
        while player_total < 21:
            print(f"\tYour cards: {player_cards}, current score: {player_total}")
            print(f"\tComputer's first card: {computer_cards[0]}")

            y_or_n = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
            print()

            if y_or_n == "y":
                player_cards.append(deal_cards())
                player_total = calculate_score(player_cards)

            elif y_or_n == "n":
                break
            else:
                print("You entered a wrong value!")

        if computer_total < 17:
            while computer_total < 17:
                computer_cards.append(deal_cards())
                computer_total = calculate_score(computer_cards)

    if player_total <= 21:
        if computer_total > 21:
            print(f"\tYour score: {player_cards} = {player_total}, Computer score: {computer_cards} = {computer_total}")
            print("YOU WIN!\n")
            bank += bet_amount
            print(f"Bank: ${bank}\n")
        elif player_total > computer_total:
            print(f"\tYour score: {player_cards} = {player_total}, Computer score: {computer_cards} = {computer_total}")
            print("YOU WIN!\n")
            bank += bet_amount
            print(f"Bank: ${bank}\n")
        elif player_total < computer_total:
            print(f"\tYour score: {player_cards} = {player_total}, Computer score: {computer_cards} = {computer_total}")
            print("YOU LOSE!\n")
            bank -= bet_amount
            print(f"Bank: ${bank}\n")
        else:
            print(f"\tYour score: {player_cards} = {player_total}, Computer score: {computer_cards} = {computer_total}")
            print("DRAW!\n")
            print(f"Bank: ${bank}\n")
    elif player_total > 21:
        print(f"\tYour score: {player_cards} = {player_total}\n\tComputer's first card: {computer_cards[0]}")
        print("You went over 21. YOU LOSE!\n")
        bank -= bet_amount
        print(f"Bank: ${bank}\n")

    if bank == 0:
        print("GAME OVER !")
        choice = input("Would you like to restart the game? (Y)es or (N)o\t").lower()
        print()
        while choice != "y" and choice != "n":
            print("You entered a wrong value!")
            choice = input("Would you like to restart the game? (Y)es or (N)o\t").lower()
            print()
        if choice == "y":
            bank = 1000
        else:
            print("Good bye!")
            break
    else:
        choice = input("Would you like to (C)ontinue, (Q)uit and cash out, or (R)estart the game? ").lower()
        print()
        while choice != "c" and choice != "q" and choice != "r":
            print("You entered a wrong value!")
            choice = input("Would you like to (C)ontinue, (Q)uit and cash out, or (R)estart the game? ").lower()
            print()
        if choice == "c":
            choice = "y"
        elif choice == "q":
            print(f"You left the game with ${bank}. We hope to see you again :)")
        else:
            bank = 1000
            choice = "y"

            