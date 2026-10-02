# ATM CODE
AB = int(5000)
atm_pin = 1234
pin = int(input("Enter your pin: "))

if pin == atm_pin:
    print("1. Withdrawal")
    print("2. Deposit")
    option = input("Choose your service 1 or 2: ").strip()
    
    if option == "1":
        withdrawal_amount = int(input("Enter the withdrawal amount: "))
        if withdrawal_amount <= AB:
            print("Withdrawal successful.")
            AB = AB - withdrawal_amount
            print("Account balance: ", AB)
        else:
            print("Insufficient balance.")
            
    elif option == "2":
        deposit_amount = int(input("Enter the deposit amount: "))
        print("Deposited successfully.")
        AB = AB + deposit_amount
        print("Account balance: ", AB)
else:
    print("Invalid pin, Access denied.")
