total = 0
number_of_items = int(input("How many items would you like to check"))
for i in range(number_of_items):
    item_price = float(input("Price of item:"))
    total = total + item_price
if total >= 100:
    total = total * 0.9
print("Total price for", number_of_items, "items is ${:.2f}".format(total))
