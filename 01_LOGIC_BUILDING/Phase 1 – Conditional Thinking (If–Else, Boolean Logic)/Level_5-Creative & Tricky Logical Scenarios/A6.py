def check_GP(a, b, c):
    if a/b == b/c:
        print("Given numbers are in Geometric Progression.")
    else:
        print("Given numbers are not in Geometric Progression.")

a, b, c = map(int, input("Enter three numbers(format- a, b, c): ").split(","))
check_GP(a, b, c)

##or 
"""
# Prevention from Zero division error:-
def check_GP(a, b, c):
    if b*b == a*c:
        print("Given numbers are in Geometric Progression.")
    else:
        print("Given numbers are not in Geometric Progression.")

a, b, c = map(int, input("Enter three numbers(format- a, b, c): ").split(","))
check_GP(a, b, c)
"""