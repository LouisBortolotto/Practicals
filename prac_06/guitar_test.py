from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2012, 209)

print("Guitar.get_age(gibson) expected 97, got", gibson.get_age())
print("gibson.get_age expected 97, got", gibson.get_age())
print("Guitar.get_age(another) expected 7, got", another.get_age())
print("Guitar.is_vintage(gibson) expected True, got", gibson.is_vintage())
print("Guitar.is_vintage(another) expected False, got", another.is_vintage())

print(gibson.get_age())