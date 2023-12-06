with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]

lines_test = [
    "Time:      7  15   30",
    "Distance:  9  40  200"  
]

time_lines = lines[0][5:].strip().split(" ")

time = []
for time_line in time_lines:
    if time_line.isdigit():
        time.append(int(time_line))

distance_lines = lines[1][9:].strip().split(" ")

distance = []
for distance_line in distance_lines:
    if distance_line.isdigit():
        distance.append(int(distance_line))

print(time)
print(distance)

total = 1

for i in range(len(time)):
    print(f"\n Race {i}")
    way = 0
    for j in range(time[i]):
        if (time[i] - j) * j > distance[i]:
            way = way + 1
            print(f"{j}ms -> {time[i]} - {j} = {time[i]-j} * {j} = {(time[i]-j)*j}")
            print(f"Total ways: {way}")
    total = total * way

print(total)