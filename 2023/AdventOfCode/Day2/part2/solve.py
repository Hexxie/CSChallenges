#For each game, find the minimum set of cubes 
# that must have been present. 
# What is the sum of the power of these sets?
file = open("./input.txt", "r")

#it seems that here we should find max values for each game

lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

sum = 0
for line in file:
    #parse game id
    id = int(line[5:line.rfind(":")])

    #extract games into list of games
    games = line[line.rfind(":")+2:].split(";")
    #print(games)

    power = 1
    max_red = 0
    max_green = 0
    max_blue = 0
    for game in games:
        cubes = game.strip().split(",")
        for cube in cubes:
            cube.strip()
            #there could be more cubes then 1 index
            if "red" in cube:
                #print(cube[:cube.rfind("r")])
                max_red = max(max_red, int(cube[:cube.rfind("r")]))
            elif "blue" in cube:
                #print(cube[:cube.rfind("b")])
                max_blue = max(max_blue, int(cube[:cube.rfind("b")]))
            elif "green" in cube: 
                #print(cube[:cube.rfind("g")])
                max_green = max(max_green, int(cube[:cube.rfind("g")]))
        
        print(f"Game {id}: max red {max_red}, max blue {max_blue}, max green {max_green}")
        power = max_red * max_green * max_blue

    sum = sum + power

print(sum)
