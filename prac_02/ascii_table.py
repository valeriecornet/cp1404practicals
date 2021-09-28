# 1

# Find ASCII code
character_input = input("Enter a character: ")

print("The ASCII code for {} is {}".format(character_input, ord(character_input)))

# Find character
LOWER = 33
UPPER = 127
code_input = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

# 2
while LOWER > code_input > UPPER:
    code_input = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}.".format(code_input, chr(code_input)))

# 3

for value in range(LOWER, UPPER + 1):
    print("{} {:>4}".format(value, chr(value)))

# Extension
min_Columns = 2
max_Columns = 20
columns = int(input("Enter how many columns in table: "))
while min_Columns > columns > max_Columns:
    columns = int(input("Enter how many columns in table: "))
print("Number of columns is {}".format(columns))

values = UPPER - LOWER + 1
rows = values // columns
print(rows)
value = LOWER
for row in range(rows):
    for column in range(columns):
        print("{} {:>4}".format(value, chr(value)), end="   ")
        value += 1
    print()

new_column = value
for value in range(new_column, UPPER + 1):
    print("{} {:>4}".format(value, chr(value)), end="   ")
print("\n")
