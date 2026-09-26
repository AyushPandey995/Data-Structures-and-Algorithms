def count_digits(num):
    if num.isdigit() != True:
        print("Enter valid number!")
        return
    digits = 0
    for i in num:
        digits+=1
    print(digits)

count_digits(input("Enter a number: "))