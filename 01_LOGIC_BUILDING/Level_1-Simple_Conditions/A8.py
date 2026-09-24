def temp_condition(temperature):
    if temperature<=15:
        print("Its cold!")
    elif temperature<=30:
        print("Its warm!")
    else:
        print("Its hot!")

temp_condition(int(input("Enter temperature in Celcius: ")))