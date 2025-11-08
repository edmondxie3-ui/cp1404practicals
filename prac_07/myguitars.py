from prac_07.guitar import Guitar

def main():

    guitars = load_guitars("guitars.csv")

    print("Stored Guitars: ")
    display_guitars(guitars)

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name,year, cost)
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

main()