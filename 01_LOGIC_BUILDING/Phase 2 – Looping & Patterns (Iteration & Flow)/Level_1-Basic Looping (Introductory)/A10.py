def prod_of_digits(num):
    prod = 1
    for i in num:
        prod = prod*int(i)
    print(f"Product of digits: {prod}")

prod_of_digits(input("Enter a number: "))