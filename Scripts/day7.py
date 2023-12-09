from collections import Counter

file = open("Data/day7.txt", "r")

hands = []

for line in file:
    line = line.split()
    hands.append((tuple(x for x in line[0]), int(line[1])))

def compare_hands(hand_one, hand_two):

    for i in range(len(hand_one)):
        if hand_one[i] > hand_two[i]:
            return True
        elif hand_two[i] > hand_one[i]:
            return False

def card_rank(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)

def classify_hand(hand):
    hand_type = tuple(sorted(Counter(hand).values()))
    
    if hand_type == (5,):
        return 7
    elif hand_type == (1, 4):
        return 6
    elif hand_type == (2, 3):
        return 5
    elif hand_type == (1, 1, 3):
        return 4
    elif hand_type == (1, 2, 2):
        return 3
    elif hand_type == (1, 1, 1, 2):
        return 2
    else:
        return 1

sorted_hands = [hands[0]]
hands = hands[1:]

while hands:
    to_add = hands.pop(0)
    pos = 0

    while True:

        if pos == len(sorted_hands):
            sorted_hands = sorted_hands + [to_add]
            break

        new_hand = [classify_hand(to_add[0])] + [card_rank(card) for card in to_add[0]]
        old_hand = [classify_hand(sorted_hands[pos][0])] + [card_rank(card) for card in sorted_hands[pos][0]]

        if compare_hands(new_hand, old_hand):
            pos += 1
            continue
        else:
            sorted_hands = sorted_hands[:pos] + [to_add] + sorted_hands[pos:]
            break

print(f"Part one: {sum(sorted_hands[i][1] * (i+1) for i in range(len(sorted_hands)))}")

def card_rank_jokers(card):
    if card == "A":
        return 13
    elif card == "K":
        return 12
    elif card == "Q":
        return 11
    elif card == "J":
        return 1
    elif card == "T":
        return 10
    else:
        return int(card)

def classify_hand_jokers(hand):
    hand = [card for card in hand if card != "J"]

    if len(hand) == 0:
        return 7
    
    hand_type = tuple(sorted(Counter(hand).values()))

    n_jokers = 5 - len(hand)
    hand_type = hand_type[:-1] + (hand_type[-1] + n_jokers,)
    
    if hand_type == (5,):
        return 7
    elif hand_type == (1, 4):
        return 6
    elif hand_type == (2, 3):
        return 5
    elif hand_type == (1, 1, 3):
        return 4
    elif hand_type == (1, 2, 2):
        return 3
    elif hand_type == (1, 1, 1, 2):
        return 2
    else:
        return 1

hands = sorted_hands
sorted_hands = [hands[0]]
hands = hands[1:]

while hands:
    to_add = hands.pop(0)
    pos = 0

    while True:

        if pos == len(sorted_hands):
            sorted_hands = sorted_hands + [to_add]
            break

        new_hand = [classify_hand_jokers(to_add[0])] + [card_rank_jokers(card) for card in to_add[0]]
        old_hand = [classify_hand_jokers(sorted_hands[pos][0])] + [card_rank_jokers(card) for card in sorted_hands[pos][0]]

        if compare_hands(new_hand, old_hand):
            pos += 1
            continue
        else:
            sorted_hands = sorted_hands[:pos] + [to_add] + sorted_hands[pos:]
            break

print(f"Part two: {sum(sorted_hands[i][1] * (i+1) for i in range(len(sorted_hands)))}")
