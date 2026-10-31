
balance = 5000

transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):

    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance += amount
        transactions.append("Deposit: " + str(amount))
        print("Amount Deposited")

    elif choice == 2:

        if amount <= balance and amount <= 10000:
            balance -= amount
            transactions.append("Withdraw: " + str(amount))
            print("Amount Withdrawn")
        else:
            print("Insufficient balance or limit exceeded")

    else:
        print("Invalid choice")

print("\nTransaction Summary")

for transaction in transactions:
    print(transaction)

print("Available Balance: Rs.", balance)
