
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

prepared = []
served = []
leftover = []

total_waste = 0
total_prepared = 0

for day in days:

    print("\n", day)

    p = int(input("Enter meals prepared: "))
    s = int(input("Enter meals served: "))

    if p < 0 or s < 0 or s > p:
        print("Invalid input")
        continue

    waste = p - s

    prepared.append(p)
    served.append(s)
    leftover.append(waste)

    total_waste += waste
    total_prepared += p

    percentage = (waste / p * 100) if p > 0 else 0

    print("Leftover Meals:", waste)
    print("Waste Percentage:", round(percentage, 2), "%")

    if percentage > 20:
        print("High Food Waste Detected")
    else:
        print("Food Waste Under Control")

print("\nWEEKLY FOOD WASTE REPORT")

print("Total Meals Prepared:", total_prepared)
print("Total Meals Wasted:", total_waste)

if total_prepared > 0:
    waste_percentage = (total_waste / total_prepared) * 100
    print("Overall Waste Percentage:",
          round(waste_percentage, 2), "%")
else:
    print("No meals prepared")
