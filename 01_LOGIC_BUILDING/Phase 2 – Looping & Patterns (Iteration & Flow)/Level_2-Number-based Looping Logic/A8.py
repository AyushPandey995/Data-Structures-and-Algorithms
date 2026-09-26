"""
def prime_num(num):
    if num <=1:
        print('Enter valid number!')
        return
    count= 0
    for i in range(1, num):
        if num%i == 0:
            count +=1
    if count == 1:
        print("The number is prime")
    else:
        print("Number is not prime")

prime_num(int(input("Enter a number: ")))
"""
###OR better version

def prime_num(num):
    if num <=1:
        print('Enter valid number!')
        return
    prime = True
    for i in range(2, num):
        if num% i == 0:
            prime = False
            break
    if not prime:
        print("Number is not prime")
    else:
        print("Number is prime")
prime_num(int(input("Enter a number: ")))