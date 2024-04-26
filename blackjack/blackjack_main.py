from random import shuffle
import os
from art import logo


# Define card attributes
suits = ('♠','♦','♥','♣')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
          '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Clear console function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define deck class
class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        shuffle(self.all_cards)

    def give_a_card(self):
        return self.all_cards.pop()

# Define player class
class Player:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.hand = []

    def place_bet(self):
        while True:
            print(f"\nYour Balance: {self.balance}\n")   
            try:
                bet = int(input("How much would you like to Bet?  "))
                clear_console()
                if bet > self.balance:
                    print(f"{self.name}, you can't bet more than your balance of {self.balance}\n")
                elif bet <= 0:
                    print(f"{self.name}, your bet can't be zero or negative!\n")
                else:
                    self.balance -= bet
                    return bet
            except ValueError:
                print("Please enter a valid amount!")

    def win_bet(self, bet_value):
        self.balance += bet_value * 2
        print(f"Congratulations {self.name}, you win! New balance is {self.balance}")

    def lose_bet(self, bet_value):
        print(f"Sorry {self.name}, you lost this bet. New balance is {self.balance}")


def calculate_hand_value(hand):
    total = sum(card.value for card in hand)
    # Adjust for Aces if the total is greater than 21
    aces = sum(1 for card in hand if card.rank == 'Ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Game Logic
def play_game():
    print(logo)
    name = input("What is your name? ")
    balance = int(input(f"Hello {name}, how much would you like to bet today? "))
    player = Player(name, balance)

    game_on = True
    while game_on:
        deck = Deck()
        player.hand = [deck.give_a_card(), deck.give_a_card()]
        dealer_hand = [deck.give_a_card(), deck.give_a_card()]
        print("Initial cards:")
        for card in player.hand:
            print(card)

        bet = player.place_bet()

        # Game decisions (Hit or Stand)
        while True:
            player_total = calculate_hand_value(player.hand)
            print(f"Current hand value: {player_total}")
            player_action = input("Do you want to HIT or STAND? ").lower()
            if player_action == "hit":
                player.hand.append(deck.give_a_card())
                print("New card:", player.hand[-1])
                player_total = calculate_hand_value(player.hand)
                if player_total > 21:
                    print("Bust! Your total is over 21.")
                    player.lose_bet(bet)
                    break
            elif player_action == "stand":
                dealer_total = calculate_hand_value(dealer_hand)
                while dealer_total < 17:
                    dealer_hand.append(deck.give_a_card())
                    dealer_total = calculate_hand_value(dealer_hand)
                    print("Dealer hits and receives:", dealer_hand[-1])
                print(f"Dealer's final hand value: {dealer_total}")
                if dealer_total > 21 or player_total > dealer_total:
                    player.win_bet(bet)
                elif player_total == dealer_total:
                    print("Draw game!")
                else:
                    player.lose_bet(bet)
                break
            else:
                print("Invalid choice, please choose 'HIT' or 'STAND'.")

        # Check to continue playing
        if player.balance > 0:
            continue_game = input("Do you want to play again? (yes/no) ").lower()
            game_on = continue_game == "yes"
            clear_console()
        else:
            clear_console()
            print(logo)
            print("You're out of money! Thanks for playing.")
            game_on = False

if __name__ == "__main__":
    play_game()
