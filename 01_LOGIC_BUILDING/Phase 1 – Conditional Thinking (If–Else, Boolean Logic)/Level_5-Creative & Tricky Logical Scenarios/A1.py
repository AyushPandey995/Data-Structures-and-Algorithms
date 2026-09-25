def check_axis(x, y):
    if x == 0 and y == 0:
        print("Point lies at the Origin")
    elif y == 0:
        print("Point lies on the X-axis")
    elif x == 0:
        print("Point lies on the Y-axis")
    else:
        print("Point lies neither on X-axis nor Y-axis")


x = int(input("Enter value of X: "))
y = int(input("Enter value of Y: "))

check_axis(x, y)