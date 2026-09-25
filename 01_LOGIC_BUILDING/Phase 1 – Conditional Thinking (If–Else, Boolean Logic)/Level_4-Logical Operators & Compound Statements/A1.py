def check_char(char):
    if len(char) != 1:
        print("Enter a single character!")
    elif char.isalpha():
        print("Its an alphabet")
    elif char.isdigit():
        print("Its a digit")
    else:
        print("Neither an alphabet nor a digit")

check_char(input("Enter a character: "))