"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# If the input given is a letter instead of a number from the 'int'
2. When will a ZeroDivisionError occur?
# If the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Have a while loop for the user. If they input a 0, ask again until it is a valid number.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
print("Finished.")