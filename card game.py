#card game

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

players=int(input("Enter the number of players: "))
cards_per_player=int(input("Enter the number of cards per player: "))

for i in range(players):
    hand = deck[i*cards_per_player:(i+1)*cards_per_player]
    print(f"Player {i+1}'s hand: {hand}")   
