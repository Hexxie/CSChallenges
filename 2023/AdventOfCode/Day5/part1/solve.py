with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]

# lines could be empty in file, check that!
lines_test = [
    "seeds: 79 14 55 13",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

is_seed_to_soil = False
is_soil_to_fertilizer = False
is_fertilizer_to_water = False
is_water_to_light = False
is_light_to_temperature = False
is_temperature_to_humidity = False
is_humidity_to_location = False

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

def fill_the_map(map, line):
    parsed_line = line.split(" ")
    map.append(parsed_line)
    #print(f"Map: {map}")

seeds = []

def get_next_value(seed, map):
    seed_val = int(seed)
    for item in map:
        dest = int(item[0])
        source = int(item[1])
        len = int(item[2])
        #print(f"{dest} {source} {len}")
        if int(seed_val) >= source and int(seed_val) <= source+len:
            #print(f"seed {seed}: {dest - source + seed_val}")
            return dest - source + seed_val
    #print(f"seed {seed}: {seed}")
    return seed


for line in lines:
    #print(len(line))
    if len(line) == 0:
        continue
    if "seeds:" in line:
        seeds = line[6:].strip().split(" ")
        print(f"Seeds: {seeds}")
        continue
    elif "seed-to-soil" in line:
        is_seed_to_soil = True
        continue
    elif "soil-to-fertilizer" in line:
        is_seed_to_soil = False
        is_soil_to_fertilizer = True
        continue
    elif "fertilizer-to-water" in line:
        is_soil_to_fertilizer = False
        is_fertilizer_to_water = True
        continue
    elif "water-to-light" in line:
        is_fertilizer_to_water = False
        is_water_to_light = True
        continue
    elif "light-to-temperature" in line:
        is_water_to_light = False
        is_light_to_temperature = True
        continue
    elif "temperature-to-humidity" in line:
        is_light_to_temperature = False
        is_temperature_to_humidity = True
        continue
    elif "humidity-to-location" in line:
        is_temperature_to_humidity = False
        is_humidity_to_location = True
        continue

    if is_seed_to_soil:
        #print("\nseed_to_soil\n")
        fill_the_map(seed_to_soil, line)
    if is_soil_to_fertilizer:
        #print("\nsoil_to_fertilizer\n")
        fill_the_map(soil_to_fertilizer, line)
    elif is_fertilizer_to_water:
        #print("\nfertilizer_to_water\n")
        fill_the_map(fertilizer_to_water, line)
    elif is_water_to_light:
        #print("\nwater_to_light\n")
        fill_the_map(water_to_light, line)
    elif is_light_to_temperature:
        #print("\nlight_to_temperature\n")
        fill_the_map(light_to_temperature, line)
    elif is_temperature_to_humidity:
        # print("\ntemperature_to_humidity\n")
        fill_the_map(temperature_to_humidity, line)
    elif is_humidity_to_location:
        #print("\nhumidity_to_location\n")
        fill_the_map(humidity_to_location, line)

locations = []
for seed in seeds:
    #print("seed_to_soil\n")
    soil = get_next_value(seed, seed_to_soil)
    #print("soil_to_fertilizer\n")
    fertilizer = get_next_value(soil, soil_to_fertilizer)
    #print("fertilizer_to_water\n")
    water = get_next_value(fertilizer, fertilizer_to_water)
    #print("water_to_light\n")
    light = get_next_value(water, water_to_light)
    #print("light_to_temperature\n")
    temperature = get_next_value(light, light_to_temperature)
    #print("temperature_to_humidity\n")
    humidity = get_next_value(temperature, temperature_to_humidity)
    #print("humidity_to_location\n")
    location = get_next_value(humidity, humidity_to_location)
    locations.append(int(location))
    #print(f"seed {seed}: location {location}")


print(min(locations))