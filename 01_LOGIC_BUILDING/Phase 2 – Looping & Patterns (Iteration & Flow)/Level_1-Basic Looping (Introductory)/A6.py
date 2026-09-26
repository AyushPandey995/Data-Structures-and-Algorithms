def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    print(f"Sum of all natural numbers till {n} :- {s}")

sum(int(input("Enter a number: ")))
