"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_income_report(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for month_number in range(1, months + 1):
        income = incomes[month_number - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_number, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month_number in range(1, months + 1):
        income = float(input("Enter income for month {}: ".format(month_number)))
        incomes.append(income)

    print_income_report(incomes, months)




main()