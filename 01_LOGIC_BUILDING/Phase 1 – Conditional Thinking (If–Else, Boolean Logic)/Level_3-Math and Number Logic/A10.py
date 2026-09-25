def check_perf_sqre(num):
    if num<0:
        print("Enter valid input!")
    else:
        i = 0
        mult = 0
        while (mult <= num):
            mult = i*i
            
            if num == mult:
                print(f"{num} is a perfect square of {i}")
                break
            i+=1
        else:
            print(f"{num} is not a perfect square")

check_perf_sqre(int(input("Enter a +ve number: ")))

