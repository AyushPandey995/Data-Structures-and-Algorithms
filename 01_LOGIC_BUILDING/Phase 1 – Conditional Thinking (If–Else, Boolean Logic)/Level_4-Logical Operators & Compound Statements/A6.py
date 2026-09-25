def check_number(num1, num2):
    if num1>0 and num2>0 and ((num1+num2)<100):
        print("Both numbers are +ve and sum is less than 100")
    elif num1>0 and num2>0:
        print("Both number are +ve but sum is greater or equal to 100")
    elif num1+num2<100:
        print("Numbers are not +ve but sum is less than 100")
    else:
        print("Neither both numbers are +ve nor sum is less than 100")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

check_number(num1, num2)