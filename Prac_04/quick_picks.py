import random

AMOUNT_OF_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
random_number = 0

quick_picks = int(input("How many quick picks would you like to generate"))

random_numbers = []

for i in range(quick_picks):
    for number in range(AMOUNT_OF_NUMBERS):
        while random_number in random_numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        random_numbers.append(random_number)
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(random_numbers[0], random_numbers[1], random_numbers[2],
                                                       random_numbers[3], random_numbers[4], random_numbers[5]))
    random_numbers = []
