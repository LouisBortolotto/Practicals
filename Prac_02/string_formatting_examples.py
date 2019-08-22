
"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

# produce the following output:
#   0
#  50
# 100

for i in range(3):
    print("{:>3}".format(i * 50))
# What did you see on line 1? 5
# What was the smallest number you could have seen, what was the largest? smallest: 5, largest: 20
# What did you see on line 2? 7
# What was the smallest number you could have seen, what was the largest? smallest: 3, largest: 0
# Could line 2 have produced a 4? No
# What did you see on line 3? 3.5853000750468484
# What was the smallest number you could have seen, what was the largest?smallest: 2.5, largest: 5.5
