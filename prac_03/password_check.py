MINIMUM_LENGTH = 4


def main():
    password = determine_password(MINIMUM_LENGTH)
    print('*' * len(password))


def determine_password(minimum_length):
    password = str(input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH)))
    while len(password) < minimum_length:
        print("Password too short")
        password = str(input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH)))
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
