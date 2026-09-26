def Armstrong_num(num):
    length = len(str(num))
    total = 0
    for i in str(num):
        total = int(i)**length + total
    if num == total:
        print(f"{num} is an Armstrong number")
    else:
        print("Not an Armstrong number")

Armstrong_num(int(input('Enter a number: ')))