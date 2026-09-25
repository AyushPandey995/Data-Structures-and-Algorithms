def pythagorean_trip(num1, num2, num3):
    if num1<=0 or num2<=0 or num3<=0:
        print("Enter positive numbers!")
    elif ((num1**2 + num2**2) == num3**2) or ((num2**2 + num3**2) == num1**2) or ((num1**2 + num3**2) == num2**2):
        print("The numbers form a Pythagorean Triplet")
    else:
        print("Does not form Pythagorean Triplet")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

pythagorean_trip(num1, num2, num3)