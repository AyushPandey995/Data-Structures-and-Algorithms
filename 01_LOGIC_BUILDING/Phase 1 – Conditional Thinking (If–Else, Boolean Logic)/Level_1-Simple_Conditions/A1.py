
def check_no(number):
    if number == 0:
        print("Number is Zero")
    elif number > 0:
        print("Number is Positive")
    else:
        print("Number is Negative")


check_no(int(input("Enter a number: ")))