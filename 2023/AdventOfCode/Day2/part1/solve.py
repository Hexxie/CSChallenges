# Determine which games would have been possible
# if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes.
file = open("./input.txt", "r")

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

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
    print(f"Game id: {id}")

    #extract games into list of games
    games = line[line.rfind(":")+2:].split(";")
    #print(games)

    skip_the_game = False
    for game in games:
        cubes = game.strip().split(",")
        print(cubes)

        red = 0
        green = 0
        blue = 0
        for cube in cubes:
            cube.strip()
            #there could be more cubes then 1 index
            if "red" in cube:
                #print(cube[:cube.rfind("r")])
                red = red + int(cube[:cube.rfind("r")])
            elif "blue" in cube:
                #print(cube[:cube.rfind("b")])
                blue = blue + int(cube[:cube.rfind("b")])
            elif "green" in cube: 
                #print(cube[:cube.rfind("g")])
                green = green + int(cube[:cube.rfind("g")])

        if green > MAX_GREEN_CUBES or blue > MAX_BLUE_CUBES or red > MAX_RED_CUBES:
            skip_the_game = True
            print(f"Game {id} skipped: {green} green, {blue} blue, {red} red")
            break

    if not skip_the_game:
        print(f"Current sum {sum}. Add game {id}")
        sum = sum + id

print(sum)
