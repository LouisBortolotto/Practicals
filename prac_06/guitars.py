from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name =")

while not name == "":

    year = input("Year: ")
    cost = input("Cost: ")

    name = Guitar(name, int(year), float(cost))
    guitars.append(name)

    name = input("Name: ")

guitar_count = 0
for guitar in guitars:
    guitar_count = guitar_count + 1
    if guitar.is_vintage():
        vintage = "vintage"
    else:
        vintage = ""
    print("Guitar", guitar_count, guitar, vintage)
