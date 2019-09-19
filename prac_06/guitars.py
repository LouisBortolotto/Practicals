from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name =")
while not name == "":
    year = input("Year: ")
    cost = input("Cost: ")
    guitar = Guitar(name, int(year), float(cost))
    guitars.append(guitar)
    name = input("Name: ")

for guitar_count, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        vintage = "vintage"
    else:
        vintage = ""
    print("Guitar", guitar_count, guitar, vintage)
