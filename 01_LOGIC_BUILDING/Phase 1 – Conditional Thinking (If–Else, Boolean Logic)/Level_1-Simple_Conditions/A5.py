"""
def leap_year(year):
    if str(year).endswith("00"):
        if year % 400 == 0:
            print("It's a leap year.")
        else:
            print("Not a leap year.")
    elif year % 4 == 0:
        print("It's a leap year.")
    else:
        print("Not a leap year")

leap_year(int(input("Enter a year ( Ex.- 2005, 1605, etc): ")))"""

##OR

def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("It's a leap year.")
    else:
        print("Not a leap year")

leap_year(int(input("Enter a year ( Ex.- 2005, 1605, etc): ")))

