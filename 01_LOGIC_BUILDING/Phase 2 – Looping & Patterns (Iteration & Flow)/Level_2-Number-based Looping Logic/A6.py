def perfect_num(num):
    if num <1 :
        print("Enter valid number!")
        return
    total = 0
    for i in range(1,num):
        if num%i == 0:
            total = i+total
    if total == num:
        print("Its a perfect number")
    else:
        print("Not a perfect number")

perfect_num(int(input("Enter a number: ")))

