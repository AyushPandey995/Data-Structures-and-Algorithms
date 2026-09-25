def check_alpha_range(alphabet):
    if len(alphabet) != 1 or not alphabet.isalpha():
        print("Please enter a single alphabet(a-z/A-Z)")
    elif "a"<=alphabet.lower()<="m":
        print("Range: A - M")
    else:
        print("Range: N - Z")

check_alpha_range(input('Enter an alphabet(a-z/A-Z): '))