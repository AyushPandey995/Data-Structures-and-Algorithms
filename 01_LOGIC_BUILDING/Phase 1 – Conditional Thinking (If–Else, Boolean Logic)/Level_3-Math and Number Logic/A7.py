def check_amount(amount):

    if amount % 2000 == 0 and amount % 500 == 0 and amount % 100 == 0:
        print("Amount can be evenly divided into 2000, 500, and 100 notes.")
    else:
        print("Amount cannot be evenly divided into all three denominations.")


amount = int(input("Enter amount: "))

check_amount(amount)