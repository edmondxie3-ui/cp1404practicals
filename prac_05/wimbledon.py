"""
Wimbledon
Estimate: 30 minutes
Actual: 78 minutes
"""



FILENAME = "wimbledon.csv"
def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        parts = [line.strip().split(",") for line in in_file]
    return parts

def count_champions(data):
    champions = {}
    for part in data:
        champion = part[2]
        champions[part[2]] = champions.get(part[2], 0) + 1
    return champions

def get_countries(data):
    countries_won = {}
    for part in data:
        country = part[1]
        countries_won[part[1]] = countries_won.get(part[1], 0) + 1
    return countries_won

def main():
    data = read_wimbledon_data(FILENAME)
    champions = count_champions(data)
    countries_won = get_countries(data)

    print("Wimbledon Champions: ")
    for champion in champions:
        print(f"{champion} {champions[champion]}")

    print()
    print(f"These {len(countries_won)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries_won.keys())))

main()