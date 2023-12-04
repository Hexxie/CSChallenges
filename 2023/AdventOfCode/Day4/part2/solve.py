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

def add_to_dict(dictionary, item):
    try:
        dictionary[item] = dictionary.get(item) + 1
    except:
        dictionary[item] = 1

sum = 0
dictionary = {}
for line in file:
    #parse card id
    id = int(line[5:line.rfind(":")])
    print(f"\nCard: {id}\n")
    add_to_dict(dictionary, id)

    #extract cards into list of cards
    cards = line[line.rfind(":")+2:].split("|")
    print(cards)

    winning_cards = cards[0].strip().split(" ")
    print(f"winning cards: {winning_cards}" )

    my_cards = cards[1].strip().split(" ")
    print(f"my cards: {my_cards}" )

    print("before")
    print(dictionary)
    counter = id
    nr_of_copies = dictionary.get(id)
    for my_card in my_cards:
        for winning_card in winning_cards:
            try:
                if int(my_card) == int(winning_card):
                    print(f"matched my {my_card} with win {winning_card}")
                    counter = counter + 1

                    for i in range(nr_of_copies):
                        add_to_dict(dictionary, counter)
            except:
                pass
    print(dictionary)

for key in dictionary:
    sum = sum + dictionary[key]

print(sum)

