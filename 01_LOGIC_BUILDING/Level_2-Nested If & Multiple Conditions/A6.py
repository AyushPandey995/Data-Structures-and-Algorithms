def can_vote(age):
    if age>100 or age<1:
        print("Are you kidding.. Please enter valid age!")
    elif(age < 18):
        print("Can not vote.")
    else:
        print("Can vote.")
can_vote(int(input("Enter your age- ")))