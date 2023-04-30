print("******WELCOME TO THE PHIR  HERA PHERI BANK******")

balance = 0

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print("Amount deposited successfully.")

    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("INSUFFICIENT BALANCE")

    elif choice == '3':
        print("Your current balance is:", balance)

    elif choice == '4':
        print("***THANK YOU FOR USING PHIR HERA PHERI BANK*******")
        break

    else:
        print("Invalid choice. Please try again.")