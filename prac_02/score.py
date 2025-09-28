"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    print(score_check(score))


def score_check(score):
    if score < 0 or score > 100:
        result = ("Invalid score")
    elif score >= 90:
        result = ("Excellent")
    elif score >= 50:
        result = ("Passable")
    else:
        result = ("Bad")
    return result

main()