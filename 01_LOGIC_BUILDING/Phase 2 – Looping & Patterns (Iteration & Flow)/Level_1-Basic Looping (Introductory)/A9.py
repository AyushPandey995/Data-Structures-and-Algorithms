def factorial(num):
    fact= 1
    for i in range(num, 1, -1):
        fact = fact*i
    print(fact)

factorial(int(input("Enter a number: ")))
