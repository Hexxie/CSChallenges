file = open("./input.txt", "r")

lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"]

real_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

real_numbers_map = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

#first - convert real numbers into digits
#then use previous algo to create numbers

# 1. Iterating through the list with real numbers
#    is not the case because we have highter value first

# 2. Iterating letter by letter from thwe start is not working
#    because we have words like "eightwothree" where comparison
#    "wothree" wont work

# 3. Python - 2 iterators which should met each other in the middle

# 4. Finally I've managed to do something, but it still searches not
#    all digits (I have to investigate what digits it skipps now)

def find_digit(line):
    start_is_found = False
    end_is_found = False
    start_digit = ""
    end_digit = ""
    for i in range(1, len(line)):
        start = line[:i+1]
        end = line[-1*i:]

        print(f"{start}, {end}")

        # from the start
        if not start_is_found:
            if line[i-1].isdigit():
                start_digit = line[i-1]
                start_is_found = True
            else:
                for number in real_numbers:
                    if number in start:
                        start_digit = real_numbers_map.get(number)
                        start_is_found = True
                        break

        if not end_is_found:
            if line[len(line)-i].isdigit():
                print("here")
                end_digit = line[len(line)-i]
                end_is_found = True
            else:
                for number in real_numbers:
                    if number in end:
                        end_digit = real_numbers_map.get(number)
                        end_is_found = True
                        break
        
        if end_is_found and start_is_found:
            break

    if not start_is_found:
        if line[len(line)-1].isdigit():
            start_digit = line[len(line)-1]

    if not end_is_found:
        end_digit = start_digit

    print(f"{start_digit}, {end_digit}")
    return [start_digit, end_digit]



numbers = []

for line in file:
    print(line)
    digits = find_digit(line.strip())
    print(digits)
   #Why some digits skipped?
    numbers.append(int(f"{digits[0]}{digits[1]}"))

sum = 0

#Check numbers which a left alone (you see)
print(f"total nr: {len(numbers)}")
for number in numbers:
    print(number)
    sum = sum + number

print(sum)

#print(find_digit("mchm6"))
