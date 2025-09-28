def main():
    score = get_score()
    choice = ''
    while choice != 'Q':
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            print(score_check(score))
        elif choice == 'S':
            shown_stars(score)
        elif choice != 'Q':
            print("Invalid choice")
            print("(G)et a valid score")
            print("(P)rint result")
            print("(S)how stars")
            print("(Q)uit")
            choice = input(">>> ").upper()
    print("Farewell!")

def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score

def score_check(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def shown_stars(score):
    print('*' * int(score))

main()