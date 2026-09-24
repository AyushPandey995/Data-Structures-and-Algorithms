def div_by_3_and_5(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("Number is divisible by both 3 and 5.")
    elif (number % 3 == 0):
        print("Number is only divisible by 3 and not by 5.")
    elif (number % 5 == 0):
        print("Number is only divisible by 5 and not by 3.")
    else:
        print("Number is neither divisible by 3 nor by 5")

div_by_3_and_5(int(input("Enter a number: ")))