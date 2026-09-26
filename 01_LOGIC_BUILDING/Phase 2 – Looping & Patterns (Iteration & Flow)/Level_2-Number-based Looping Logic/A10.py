def fibinacci_sum(n):
    a = 0
    b = 1
    total = 0
    for i in range(n):
        total +=a
        a, b = b, a+b
    print(f"Sum of first {n} terms of Fibonacci series: {total}")

fibinacci_sum(int(input('Enter a number: ')))