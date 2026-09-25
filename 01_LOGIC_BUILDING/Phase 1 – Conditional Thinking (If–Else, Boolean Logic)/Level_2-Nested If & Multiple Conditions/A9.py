def check_day(date):
    if 0<date<8:    
        match date:
            case 1:
                print("Sunday")
            case 2:
                print("Monday")
            case 3:
                print("Tuesday")
            case 4:
                print("Wednesday")
            case 5:
                print("Thursday")
            case 6:
                print("Friday")
            case 7:
                print("Saturday")
            case _ :
                print("Enter date between 1-7!")
    else:
        print("Enter date between 1-7!")
check_day(int(input("Enter a date(1-7): ")))