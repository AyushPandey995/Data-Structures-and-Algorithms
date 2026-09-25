# def check_password(password):

#     if len(password)>=8 and any(char.isdigit() for char in password):
#         print('Password is valid')
#     else:
#         print("Use strong password")

# check_password(input('Enter password(length of password>=8 and contain atleast one digit): '))

# ###OR

def check_password(password):
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit=True
            break

    if len(password)>=8 and has_digit:
        print('Password is valid')
    else:
        print("Use strong password")

check_password(input('Enter password(length of password>=8 and contain atleast one digit): '))

