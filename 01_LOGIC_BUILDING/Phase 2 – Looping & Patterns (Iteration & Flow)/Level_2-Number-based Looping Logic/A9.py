def fibonacci_series(num):
    series = []
    value = 0
    total = 0
    for i in range(0, num):
        total = i + value
        value = total
        series.append(total)

    print(series)
fibonacci_series(int(input("Enter a number: ")))