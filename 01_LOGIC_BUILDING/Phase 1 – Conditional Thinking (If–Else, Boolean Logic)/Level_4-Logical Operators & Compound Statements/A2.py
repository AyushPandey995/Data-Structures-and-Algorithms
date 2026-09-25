def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num%5 == 0:
        print("Buzz")
    elif num%3 == 0:
        print("Fizz")
    else:
        print("Neither divisible by 3 nor by 5")

fizz_buzz(int(input('Enter a number: ')))