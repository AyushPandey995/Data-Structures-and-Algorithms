def check_quarant(num1, num2):
    print(f"Entered value: ({num1}, {num2})")
    if num1 > 0 and num2 > 0:
        print("1st Quadrant")
    elif num1 < 0 and num2 > 0:
        print("2nd Quadrant")
    elif num1 < 0 and num2 < 0:
        print("3rd Quadrant")
    elif num1 > 0 and num2 < 0:
        print("4th Quadrant")
    elif num1 == 0 and num2 > 0:
        print("+ve Y-axis")
    elif num1 == 0 and num2 < 0:
        print("-ve Y-axis")
    elif num1 > 0 and num2 == 0:
        print("+ve X-axis")
    elif num1 < 0 and num2 == 0:
        print("-ve X-axis")
    elif num1 == 0 and num2 == 0:
        print("Its origin")
    else:
        print("Enter valid quadrant value!")

num1 = int(input("Enter value of X: "))
num2 = int(input("Enter value of Y: "))

check_quarant(num1, num2)