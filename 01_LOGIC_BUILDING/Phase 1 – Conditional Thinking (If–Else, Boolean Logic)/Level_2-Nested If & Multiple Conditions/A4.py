def check_multiple(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Enter Non-zero numbers!") 
    elif num1%num2 == 0 or num2%num1 == 0:
        print("Numbers are multiple of each other.")
    else:
        print("Not a multiple of each other!")
num1 = int(input("Enter first no.: "))
num2 = int(input("Enter second no.: "))
check_multiple(num1, num2)