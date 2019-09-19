from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2012, 209)

print(Guitar.get_age(gibson))
print(gibson.get_age())
print(Guitar.get_age(another))
print(Guitar.is_vintage(gibson))
print(Guitar.is_vintage(another))

print(Guitar.get_age(gibson))