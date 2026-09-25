"""
For example, suppose the rates are:

Units consumed	Rate
0–100	₹5/unit
101–200	₹7/unit
201–300	₹10/unit
Above 300	₹15/unit

The important point is that electricity slabs are usually progressive. For example, if you use 250 units:

First 100 → 100 × ₹5
Next 100 → 100 × ₹7
Remaining 50 → 50 × ₹10
"""

def electricity_bill(units):
    if units<0:
        print("Enter valid consumed units!")
    elif units<=100:
        print(f"Bill:- {units*5}Rs")
    elif units<=200:
        print(f"Bill:- {(100*5)+((units-100)*7)}Rs")
    elif units<=300:
        print(f"Bill:- {(100*5)+(100*7)+((units-200)*10)}Rs")
    else:
        print(f"Bill:- {(100*5)+(100*7)+(100*10)+((units-300)*15)}Rs")

electricity_bill(int(input("Enter the units of electricity consumed: ")))