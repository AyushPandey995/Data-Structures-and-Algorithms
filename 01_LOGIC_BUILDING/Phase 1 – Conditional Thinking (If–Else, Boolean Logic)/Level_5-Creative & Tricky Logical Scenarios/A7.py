def check_digits(num):
    num = str(num)

    if int(num[0]) + int(num[2]) == int(num[1]):
        print("Sum of first and last digit equals the middle digit")
    else:
        print("Sum of first and last digit does not equal the middle digit")


num = int(input("Enter a 3-digit number: "))

check_digits(num)