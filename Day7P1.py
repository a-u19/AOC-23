import re
from functools import cmp_to_key
from collections import Counter

def OpenFile(file):
    with open(file,"r") as file:
        data = file.read()
    return data

def HandRankingsType(hand):
    counts = sorted(Counter(hand).values(), reverse=True)
    if counts[0] == 5:
        return 6
    if counts[0] == 4:
        return 5
    if counts[0] == 3 and counts[1] == 2:
        return 4
    if counts[0] == 3:
        return 3
    if counts[0] == 2 and counts[1] == 2:
        return 2
    if counts[0] == 2:
        return 1
    return 0  

def CompareSameRanks(a,b):
    type_a = HandRankingsType(a[0])
    type_b = HandRankingsType(b[0])
    card_rankings = "23456789TJQKA"
    if type_a>type_b:
        return 1
    elif type_b>type_a:
        return -1
    for card_a,card_b in zip(a[0],b[0]):
        if card_a == card_b:
            continue
        elif card_rankings.index(card_a) > card_rankings.index(card_b):
            return 1
        else:
            return -1

def main(input):
    regex = r'(\w{5}) (\d+)'
    hands = re.findall(regex, OpenFile(input))
    # print(hands)
    hands.sort(key=cmp_to_key(CompareSameRanks))
    # print(hands)
    total = 0
    for i,each_hand in enumerate(hands,1):
        total += (i * int(each_hand[1]))
    print(total)
        
main("day7input.txt")