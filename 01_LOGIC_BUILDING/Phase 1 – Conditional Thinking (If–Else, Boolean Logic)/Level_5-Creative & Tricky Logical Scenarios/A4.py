def time_angle(hr, min):
    if hr>12 or hr<1 or min>59 or min<1:
        print("Enter valid time!")
        return
    min_angle = 6*min
    hr_angle = hr*30 + (min/2)
    angle = abs(min_angle-hr_angle)
    if angle > 180:
        angle = 360-angle
        
    print(f"Angle is {angle}")


hr, min = map(int, input("Enter time HH:MM - ").split(":"))
time_angle(hr, min)