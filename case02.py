
n = int(input("Enter number of products: "))

total = 0

for i in range(n):

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    if amount >= 1000:
        discount = amount * 0.10
    elif amount >= 500:
        discount = amount * 0.05
    else:
        discount = 0

    tax = amount * 0.05

    final_amount = amount - discount + tax

    total = total + final_amount

    print("\nProduct:", name)
    print("Amount:", amount)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Amount:", final_amount)

print("\nTotal Bill: Rs.", round(total, 2))

if total >= 3000:
    print("Congratulations! You are a premium customer.")
