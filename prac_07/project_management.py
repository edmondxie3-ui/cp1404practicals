"""
Project management
Estimate: 30 minutes
Actual:
"""
import datetime
from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    print("Welcome to the Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print("(L)oad projects")
    print("(S)ave projects")
    print("(D)isplay projects")
    print("(F)ilter projects by date")
    print("(A)dd new project")
    print("(U)pdate project")
    print("(Q)uit")
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")

        # elif choice == 'd':
        #
        # elif choice == 'f':
        #
        # elif choice == 'a':
        #
        # elif choice == 'u':

        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")
        choice = input(">>> ").lower()

    save_choice = input(f"Would you like to save to projects.txt? ")
    """YES OR NO"""
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, parts[2], parts[3], parts[4])
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")

        for project in projects:
            line = (
                f"{project.name}\t"
                f"{project.start_date.strftime('%d/%m/%Y')}\t"
                f"{project.priority}\t"
                f"{project.cost_estimate}\t"
                f"{project.completion_percent}\n"
            )
            file.write(line)
main()