def check_triangle(a, b, c):
    if a+b>c and b+c>a and a+c> b:
        print("Given triangle is valid.")
    else:
        print("Triangle is not valid!")

a = int(input("Enter first side of triangle- "))
b = int(input("Enter second side of triangle- "))
c = int(input("Enter third side of triangle- "))

check_triangle(a, b, c)