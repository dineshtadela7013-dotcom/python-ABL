
products = [
    ("Laptop", 50000, 5),
    ("Mobile", 20000, 10),
    ("Keyboard", 800, 0),
    ("Mouse", 500, 3),
    ("Headphones", 1500, 2)
]

total_value = 0

print("PRODUCT CATALOGUE AUDIT")

for product in products:

    name, price, stock = product

    value = price * stock

    total_value += value

    print("\nProduct:", name)
    print("Price: Rs.", price)
    print("Stock:", stock)
    print("Inventory Value: Rs.", value)

    if stock == 0:
        print("Out of Stock")

    elif stock < 3:
        print("Low Stock - Reorder Required")

    else:
        print("Stock Available")

print("\nTotal Inventory Value: Rs.", total_value)
