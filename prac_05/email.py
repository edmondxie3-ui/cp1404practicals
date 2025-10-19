"""
Emails
Estimate: 20 minutes
Actual: 34 minutes
"""

emails = {}

def find_name(given_email):
    return " ".join(given_email.split("@")[0].split(".")).title()

given_email = input("Email: ")
while given_email != "":
    name = find_name(given_email)
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    if confirmation == "" or confirmation == "y":
        emails[name] = given_email
        print(f"{emails}")
    else:
        given_name = input("Name: ")
        emails[name] = given_email
    given_email = input("Email: ")


print()
for user in emails:
    print(f"{user} ({emails[user]})")

