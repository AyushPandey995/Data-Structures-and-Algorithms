def third_angle(angle_1, angle_2):
    if angle_1 > 0 and angle_2 > 0 and angle_1 + angle_2 < 180:
        angle_3 = 180-(angle_1+angle_2)
        print(f"Third angle is {angle_3}")
    else:
        print("Enter valid angles!")

angle_1 = int(input("Enter first angle of triangle: "))
angle_2 = int(input("Enter second angle of triangle: "))

third_angle(angle_1, angle_2)