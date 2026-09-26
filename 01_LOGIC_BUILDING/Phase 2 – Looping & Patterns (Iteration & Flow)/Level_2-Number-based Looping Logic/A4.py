def sum_digits(num):
    total = 0

    for i in str(num):
        total += int(i)

    print(f"Sum of digits: {total}")


num = int(input("Enter a number: "))
sum_digits(num)
