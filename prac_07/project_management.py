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

        elif choice == 'd':
            incomplete_projects = [p for p in projects if p.completion_percent < 100]
            completed_projects = [p for p in projects if p.completion_percent == 100]

            incomplete_projects.sort()
            completed_projects.sort()

            print("Incomplete projects: ")
            for project in incomplete_projects:
                print(f"  {project}")

            print("Completed projects: ")
            for project in completed_projects:
                print(f"  {project}")

        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = [p for p in projects if p.start_date >= filter_date]
            filtered_projects.sort()
            print(f"Projects starting on or after {filter_date.strftime('%d/%m/%Y')}:")
            for project in filtered_projects:
                print(f"  {project}")

        elif choice == 'a':
            print("Let's add a new project")
            name = input("Name: ")
            date_string = input("Start date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percent = int(input("Percent complete: "))
            new_project = Project(name, start_date, priority, cost_estimate, completion_percent)
            projects.append(new_project)
            print(f"Project '{name}' added.")

        elif choice == 'u':
            for i, project in enumerate(projects):
                print(f"{i} {projects}")

            choice_index = int(input("Project choice: "))
            project_to_update = projects[choice_index]
            print(project_to_update)

            new_percent = input("New Percentage: ")
            new_priority = input("New Priority: ")

            if new_percent != "":
                project_to_update.completion_percent = int(new_percent)
            if new_priority != "":
                project_to_update.priority = int(priority)

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
            name=parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority=int(parts[2])
            cost_estimate=float(parts[3])
            completion_percent=int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percent)
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