"""
def check_century(year):
    if year.endswith("00"):
        print(f"{year[0]+year[1]}th century")
    else:
        cen = int(year[0]+year[1])
        print(f"{cen+1}th century")
        

check_century(input("Enter a year: "))
"""
##or

def check_century(year):
    if year<=0:
        print("Enter valid year!")
    else:
        century = ((year-1)//100)+1
        print(f"{century}th century")
        

check_century(int(input("Enter a year: ")))
