def check_len(num):
    l = len(str(abs(num)))
    if l > 2:
        print("Entered number is multi digit.")
    else:
        print(f"Entered number is of {l} digit length")

check_len(int(input("Enter some numbers: ")))