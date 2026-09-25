def check_presence(num):
    if 100<=num<=999:
        print("Number is in the range 100 to 999")
    else:
        print("Number is not in range")

check_presence(int(input("Enter a number: ")))