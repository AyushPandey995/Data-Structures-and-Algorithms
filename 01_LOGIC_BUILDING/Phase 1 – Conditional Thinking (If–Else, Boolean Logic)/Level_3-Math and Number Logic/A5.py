def check_7(num):
    if num % 7 == 0 and str(num).endswith("7"):
        print("Number is divisible by 7 & last digit is 7")
    elif num % 7 == 0:
        print("Number is divisible by 7")
    elif str(num).endswith("7"):
        print("Last digit is 7")
    else:
        print("Neither divisible by 7 nor last digit is 7")

check_7(int(input("Enter a number: ")))


