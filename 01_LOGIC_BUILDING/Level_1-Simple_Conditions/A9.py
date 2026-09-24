def check_alphabet(alphabet):
    if len(alphabet) != 1 or not alphabet.isalpha():
        print("Enter a sigle character(alphabet)!!")
    elif alphabet.lower().strip() in ["a", "e", "i", "o", "u"]:
        print("Its a vowel")
    else:
        print("Its a consonant")


check_alphabet(input("Enter an alphabet: "))