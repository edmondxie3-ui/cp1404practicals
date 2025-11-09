"""
Project management
Estimate: 30 minutes
Actual:
"""

from prac_07.project import Project

def main():
    print()
    print("Welcome to the Pythonic Project Management")
    print(f"Loaded __ projects from projects.txt")
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
            print("Incomplete projects: ")

            print("Completed projects: ")
        # elif choice == 's':
        #
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