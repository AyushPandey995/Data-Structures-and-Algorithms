def odd_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum += i
    print(f"Sum:- {sum}")

odd_sum(int(input("Enter a number: ")))
