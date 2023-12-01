file = open("./input.txt", "r")

#lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

numbers = []
for line in file:
   # print(f"line: {line}")
    digits = []
    for letter in line:
        if letter.isdigit():
            digits.append(letter)
   # print("digits:")
   #print(digits)
    if len(digits) == 0:
        continue
       # print("skip")
    elif len(digits) == 1:
        numbers.append(int(f"{digits[0]}{digits[0]}"))
    else:
        numbers.append(int(f"{digits[0]}{digits[-1]}"))

#print(numbers)

sum = 0
for number in numbers:
    sum = sum + number

print(sum)