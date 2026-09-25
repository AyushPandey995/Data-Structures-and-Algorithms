def check_AP(a, b, c):
    if a-b == b-c:
        print("Given numbers are in Arithmetic Progression")
    else:
        print("Given numbers are not in Arithmetic Progression")

a, b, c = map(int, input("Enter three numbers(format- a, b, c): ").split(","))
check_AP(a, b, c)