"""
Emails
Estimate: 20 minutes
Actual:
"""

emails = {}

given_email = input("Email: ")
while given_email != "":
    name = given_email.split("@")[0].replace(".", " ").title()
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

