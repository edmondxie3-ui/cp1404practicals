from prac_06.guitar import Guitar

print("My Guitars!")
guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")
    name = input("Name: ")
