def check_char(char):
    if len(char) != 1:
        print("Enter a valid single Number/Alphabet/Special_Character!") 
    elif char.isdigit():
        print("It's a Number")
    elif char.islower():
        print("It's in Lowercase")
    elif char.isupper():
        print("It's in Uppercase")
    else :
        print("It's a Special_Character")


check_char(input("Enter a a single Number/Alphabet/Special_Character: "))
    