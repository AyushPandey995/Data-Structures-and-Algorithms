def check_grade(mark):
    if mark>100 or mark<0:
        print("Enter valid marks!!")
    elif mark>85:
        print("Grade: A")
    elif mark>65:
        print("Grade: B")
    elif mark>50:
        print("Grade: C")
    elif mark>30:
        print("Grade: D")
    else:
        print("Grade: F")


check_grade(int(input("Enter your average marks: ")))