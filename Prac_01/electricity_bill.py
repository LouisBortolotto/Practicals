TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31"))
while tariff != 11 and tariff != 31:
    tariff = int(input("Which tariff? 11 or 31"))
if tariff == 11:
    kWh_price = TARIFF_11
else:
    kWh_price = TARIFF_31
kWh_use = float(input("Enter daily use in kWh"))
billing_days = int(input("Enter number of billing days"))
bill = (kWh_price * kWh_use * billing_days)
print("Estimated Bill: ${:.2f}".format(bill))
