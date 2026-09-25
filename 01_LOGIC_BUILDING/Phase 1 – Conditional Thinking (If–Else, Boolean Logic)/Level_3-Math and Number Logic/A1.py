def check_distinct(num):
    num = str(num)
    if num[0] != num[1] and num[1] != num[2] and num[0] != num[2] :
        print("All digits are distinct")
    else:
        print("Digits are not distinct")

num = int(input("Enter a 3-digit number: "))


check_distinct(num)

#We can also use set{} to do this.
"""
def check_distinct(num):

    num = str(num)

    if len(set(num)) == 3:
        print("All digits are distinct")
    else:
        print("Digits are not distinct")


num = int(input("Enter a 3-digit number: "))
check_distinct(num)
"""