def check_date(DD1, MM1, DD2, MM2):
    if MM1>MM2:
        print(f"{DD2}/{MM2} comes first")
    elif MM1<MM2:
        print(f"{DD1}/{MM1} comes first")
    elif MM1==MM2:
        if DD1>DD2:
            print(f"{DD2}/{MM2} comes first")
        elif DD1 == DD2:
            print("Both dates are same")
        else:
            print(f"{DD1}/{MM1} comes first")
    else:
        print("Enter valid dates!")


DD1, MM1 = map(int, input("Enter first date(format-DD/MM): ").split("/"))
DD2, MM2 = map(int, input("Enter second date(format-DD/MM): ").split("/"))
check_date(DD1, MM1, DD2, MM2)