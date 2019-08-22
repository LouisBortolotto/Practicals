for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(10):
    print(10 * (i + 1), end=' ')
print()

for i in range(20):
    print(20 - i, end=' ')
print()

stars = int(input("How many stars would you like to print?"))
print("*" * stars)

stars = int(input("How many stars would you like to print?"))
for i in range(stars + 1):
    print("*" * i)
