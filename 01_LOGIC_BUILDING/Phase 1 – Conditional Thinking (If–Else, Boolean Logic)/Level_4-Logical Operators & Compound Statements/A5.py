def tax_eligibility(age, income):
    if age<0 or age>120:
        print("Enter valid age!")
    elif age>18 and income>500000:
        print("You have to pay tax")
    else:
        print("You don't have to pay tax")

age = int(input("Enter your age: "))
income = int(input("Enter your income(annually): "))

tax_eligibility(age, income)