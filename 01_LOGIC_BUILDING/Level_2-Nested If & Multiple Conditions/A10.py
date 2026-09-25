"""
def days_on_month(month_no):
    if 0< month_no <13:
        match month_no:
            case 1:
                print("Month: January, No. of days: 31")
            case 2:
                print("Month: February, No. of days: 28")
            case 3:
                print("Month: March, No. of days: 31")
            case 4:
                print("Month: April, No. of days: 30")
            case 5:
                print("Month: May, No. of days: 31")
            case 6:
                print("Month: June, No. of days: 30")
            case 7:
                print("Month: July, No. of days: 31")
            case 8:
                print("Month: August, No. of days: 31")
            case 9:
                print("Month: September, No. of days: 30")
            case 10:
                print("Month: October, No. of days: 31")
            case 11:
                print("Month: November, No. of days: 30")
            case 12:
                print("Month: December, No. of days: 31")
    else:
        print("Enter valid month number(1-12)!")

days_on_month(int(input('Enter month number(1-12): ')))
"""
##OR
def days_on_month(month_no):
    if 0< month_no <13:
        match month_no:
            case 1|3|5|7|8|10|12:
                print("No of days: 31")
            case 2:
                print("No of days: 28")
            case 4|6|9|11:
                print("No of days: 30")
    else:
        print("Enter valid month number(1-12)!")
        
days_on_month(int(input('Enter month number(1-12): ')))
