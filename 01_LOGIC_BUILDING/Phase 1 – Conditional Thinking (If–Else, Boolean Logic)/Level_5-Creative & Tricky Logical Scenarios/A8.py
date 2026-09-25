def check_prod_sum(num):
    numb= int(num)
    if numb<1 or numb >9999:
        print("Enter valid number")
        return
    prod = 1
    sum = 0
    for i in num:
        prod =  prod*int(i)
        sum = sum+int(i)
    if sum>prod:
        print("Sum is greater")
    elif sum == prod:
        print("Sum and Product are equal")
    else:
        print("Product is greater")
check_prod_sum(input('Enter a nuymber (1-9999): '))