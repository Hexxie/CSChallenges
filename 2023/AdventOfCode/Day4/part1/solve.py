# Picking one up, it looks like each card has
# two lists of numbers separated by a vertical bar (|):
# a list of winning numbers and then a list of numbers you have.

# The first match makes the card worth one point
# and each match after the first doubles the point 
# value of that card.

file = open("./input.txt", "r")

lines = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

sum = 0
for line in file:
    #parse card id
    id = int(line[5:line.rfind(":")])
    print(f"\nCard: {id}\n")

    #extract cards into list of cards
    cards = line[line.rfind(":")+2:].split("|")
    print(cards)

    winning_cards = cards[0].strip().split(" ")
    print(f"winning cards: {winning_cards}" )

    my_cards = cards[1].strip().split(" ")
    print(f"my cards: {my_cards}" )

    curr_points = 0
    for my_card in my_cards:
        for winning_card in winning_cards:
            try:
                if int(my_card) == int(winning_card):
                    print(f"matched my {my_card} with win {winning_card}")
                    if curr_points == 0:
                        curr_points = 1
                    else:
                        curr_points = curr_points * 2
                    print(curr_points)
            except:
                pass
    sum = sum + curr_points
    print(f"current sum {sum}, current_points {curr_points}")
