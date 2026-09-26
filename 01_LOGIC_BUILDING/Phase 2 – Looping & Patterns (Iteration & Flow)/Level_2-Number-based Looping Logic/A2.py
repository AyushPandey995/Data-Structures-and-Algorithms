def reverse_number(num):
    reverse = ""

    for i in str(num):
        reverse = i+ reverse

    print(f"Reverse: {reverse}")



num = int(input("Enter a number: "))
reverse_number(num)