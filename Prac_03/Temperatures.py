"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(convert_celsius())
        elif choice == "F":
            print(convert_fahrenheit())
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)


def convert_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return "Result: {:.2f} C".format(celsius)


main()
