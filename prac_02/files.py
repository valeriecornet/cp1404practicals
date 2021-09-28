# 1.

name_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=name_file)
name_file.close()

# 2.

edits_file = open("name.txt", "r")
names = edits_file.read().strip()
edits_file.close()
print("Your name is {}".format(names))

# 3.

numbers_file = open("numbers.txt", "w")
#number17 = int(17)
#number42 = int(42)
#number400 = int(400)
print("17\n42\n400", file=numbers_file)
numbers_file.close()

numbers_add = open("numbers.txt", "r")
number1 = int(numbers_add.readline())
number2 = int(numbers_add.readline())
addition = number1 + number2
numbers_add.close()

print(addition)
