def check_triangle(a, b, c):
    if a+b>c and b+c>a and a+c> b:
        print("Given triangle is valid.")
        if a==b==c:
            print("Triangle is Equilateral.")
        elif a==b or a==c or b==c:
            print("Triangle is Isosceles")
        else:
            print("Tringle is Scalene")
    else:
        print("Triangle is not valid!")

a = int(input("Enter first side of triangle- "))
b = int(input("Enter second side of triangle- "))
c = int(input("Enter third side of triangle- "))

check_triangle(a, b, c)