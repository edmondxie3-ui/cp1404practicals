def main()
    password = get_password()

def get_password():
    password = input("Password: ")
    while len(password) != 10:
        print("Password not work")
        password = input("Password: ")
    print('*' * len(password))


main()