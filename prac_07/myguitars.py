from prac_07.guitar import Guitar

def main():

    guitars = load_guitars("guitars.csv")

    print("Stored Guitars: ")
    display_guitars(guitars)

    print("Add a new guitar: ")
    guitars = add_new_guitars(guitars)

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

def add_new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")
        name = input("Name: ")
    return guitars

main()