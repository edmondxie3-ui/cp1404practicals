# 1.
FILENAME = "name.txt"
name = input("Name: ")
first_file = open(FILENAME, 'w')
print(name, file=first_file)
first_file.close()

# 2.
FILENAME = "name.txt"
first_file = open(FILENAME)
text = first_file.read().strip()
first_file.close()
print(f"Hi {text}!")

# 3.
FILENAME = "numbers.txt"
second_file = open(FILENAME)
first_number = int(second_file.readline())
second_number = int(second_file.readline())
second_file.close()
total = first_number + second_number
print(total)

# 4.
FILENAME = "numbers.txt"
total_number = 0
with open(FILENAME) as second_file:
    for number in second_file:
        total_number += int(number)
print(total_number)
