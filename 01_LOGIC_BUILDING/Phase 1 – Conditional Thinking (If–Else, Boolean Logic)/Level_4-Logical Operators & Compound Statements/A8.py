def check_day(day):

    if 1 <= day <= 5:
        print("Weekday")

    elif 6 <= day <= 7:
        print("Weekend")

    else:
        print("Enter a valid weekday number (1-7)!")


day = int(input("Enter weekday number (1-7): "))

check_day(day)