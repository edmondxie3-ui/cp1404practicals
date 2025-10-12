"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data(FILENAME)
    print(data)
    display = display_data(FILENAME)

def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    nest = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        nest.append(parts)
    input_file.close()
    return nest

def display_data(filename=FILENAME):
    input_file = open(filename)
    for line in input_file:
        parts = line.strip().split(",")
        print(f"{parts[0]} is taught by {parts[1]:<12} and has {parts[2]:>3} students")
    input_file.close()
main()