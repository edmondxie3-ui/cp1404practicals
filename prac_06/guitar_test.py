from prac_06.guitar import Guitar

def main():
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16025.40)
    print(gibson_guitar)
    print(f"Gibson L-5 CES get_age() - Expected 103. Got {gibson_guitar.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson_guitar.is_vintage(gibson_guitar.get_age)}")

main()