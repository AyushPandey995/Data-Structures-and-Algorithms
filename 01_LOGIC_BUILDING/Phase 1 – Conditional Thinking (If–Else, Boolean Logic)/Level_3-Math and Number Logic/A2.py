def check_middle(num):

    num = str(num)

    a = int(num[0])
    b = int(num[1])
    c = int(num[2])

    if b > a and b > c:
        print("Middle digit is Largest")

    elif b < a and b < c:
        print("Middle digit is Smallest")

    else:
        print("Middle digit is neither largest nor smallest")


num = int(input("Enter a 3-digit number: "))

check_middle(num)

