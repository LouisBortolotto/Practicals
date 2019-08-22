"""
Louis Bortolotto
"""


def main():
    password = get_password()
    print_password(password)


def get_password():
    min_length = 10
    password = str(input("What is your password?"))
    while len(password) < min_length:
        password = str(input("password must be 10 characters or more"))
    return password


def print_password(password):
    for i in range(len(password)):
        print("*", end='')


main()
