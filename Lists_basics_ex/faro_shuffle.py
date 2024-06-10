card_deck = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    shuffled_deck = []
    half_deck_count = (len(card_deck) // 2)
    left_part = card_deck[:half_deck_count]
    right_part = card_deck[half_deck_count:]
    for index in range(half_deck_count):
        shuffled_deck.append(left_part[index])
        shuffled_deck.append(right_part[index])
    card_deck = shuffled_deck

print(shuffled_deck)
