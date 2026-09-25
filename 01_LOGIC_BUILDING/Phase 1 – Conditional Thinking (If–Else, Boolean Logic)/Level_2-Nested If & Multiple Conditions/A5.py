def greet(hour):
    if hour>23 or hour<0:
        print("Enter valid hour(0-23)!!")
    elif 4<=hour<12:
        print("Good Morning!")
    elif 12<=hour<16:
        print("Good Afternoon!")
    elif 16<=hour<21:
        print("Good Evening!")
    else:
        print("Good Night!")
greet(int(input("Enter time in hr(0-23): ")))
