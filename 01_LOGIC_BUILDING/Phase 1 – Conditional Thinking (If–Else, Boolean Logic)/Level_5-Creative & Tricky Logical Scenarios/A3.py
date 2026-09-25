def check_date(date, month):
    if date<0 or date>31 or month<0 or month>12:
        print("Enter valid date") 
    elif month in [1, 3, 5, 7, 8, 10, 12] and date<=31:
        print("Date is valid")
    elif month in [4, 6, 9, 11] and date<=30:
        print("Date is valid")
    elif month == 2 and date<=28:
        print("Date is valid")
    else:
        print("Enter valid date")
date, month = map(int, input("Enter date and month(format- date/month):").split("/"))
check_date(date, month)