def even_odd(num1, num2):
    if num1%2 == 0 and num2%2 == 0:
        print("Both numbers are Even.")
    elif num1%2 == 0 and num2%2 != 0:
        print(f"{num1} is even and {num2} is odd.")
    elif num1%2 != 0 and num2%2 == 0:
        print(f"{num2} is even and {num1} is odd.")
    else:
        print("Both numbers are Odd.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
even_odd(num1, num2)