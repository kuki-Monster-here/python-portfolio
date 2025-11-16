import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(cards)

player_hand = [cards.pop(), cards.pop()]
dealer_hand = [cards.pop(), cards.pop()]

print(f"Твои карты: {player_hand}, сумма: {sum(player_hand)}")
print(f"Карты дилера: [{dealer_hand[0]}, ?]")
