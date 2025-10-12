import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    pick_amount = int(input("How many quick picks? "))
    for i in range(pick_amount):
        pick = quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

def quick_pick():
    pick = []
    while len(pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in pick:
            pick.append(number)
    pick.sort()
    return pick

main()