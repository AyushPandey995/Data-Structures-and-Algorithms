def palindrome(num):
    reverse = ""
    for i in str(num):
        reverse = i + reverse

    if reverse == str(num):
        print("Its a palindrome")
    else:
        print("Not a palindrome")

palindrome(int(input("Enter a number: ")))