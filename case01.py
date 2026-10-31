
units_list = [80, 150, 250, 320]

fixed_charge = 50

bills = []

for units in units_list:

    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3

    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    total = bill + fixed_charge

    bills.append(total)

    print("Units:", units)
    print("Electricity Bill: Rs.", total)
    print("----------------------")

print("Monthly Bill Comparison:")

for i in range(len(bills)):
    print("Month", i + 1, ":", bills[i])

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 100:
            print("Unusual increase detected!")
