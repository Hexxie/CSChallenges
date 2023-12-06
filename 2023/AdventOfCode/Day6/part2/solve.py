with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]

lines_test = [
    "Time:      7  15   30",
    "Distance:  9  40  200"  
]

time = int(lines[0][5:].strip().replace(" ", ""))
distance = int(lines[1][9:].strip().replace(" ", ""))

print(time)
print(distance)

total = 1


way = 0
for j in range(time):
    if (time - j) * j > distance:
        way = way + 1
        print(f"{j}ms -> {time} - {j} = {time-j} * {j} = {(time-j)*j}")
        print(f"Total ways: {way}")
total = total * way

print(total)