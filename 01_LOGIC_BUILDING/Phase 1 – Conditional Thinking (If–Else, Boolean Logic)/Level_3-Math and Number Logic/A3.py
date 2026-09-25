def first_last(num):

    num = str(num)

    a = int(num[0])
    b = int(num[3])

    if a == b:
        print("First and Last digit are same")
    else:
        print("First and Last digit are not same")


num = int(input("Enter a 4-digit number: "))

first_last(num)
