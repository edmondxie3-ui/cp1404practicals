COLOURS = {"Asparagus": "#87a96b", "Aureolin": "#fdee00", "Beaver": "#9f8170", "Beige": "#f5f5dc", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Apricot": "#fbceb1", "Aqua": "#00ffff", "Bistre": "#3d2b1f"}

choice = input("Colour: ").capitalize()
while choice != "":
    if choice in COLOURS:
        print(f"{choice} is {COLOURS[choice]}")
        choice = input("Colour: ")
    else:
        print("Invalid colour name")
        choice = input("Colour: ")