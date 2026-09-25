def am_pm(Hr, Min):
    if Hr<0 or Hr>23 or Min<0 or Min>59:
        print("Enter valid time!)")
    elif Hr<12:
        print("Its AM")
    else:
        print("Its PM")

Hr, Min = map(int, input("Enter time HH:MM: ").split(":"))
am_pm(Hr, Min)