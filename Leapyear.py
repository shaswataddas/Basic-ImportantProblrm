year = int(input())
istrue = True

if year%100==0:
    if year%400==0:
        istrue=True
    else:
        istrue=False
else:
    if year%4==0:
        istrue=True
    else:
        istrue=False
print("Leap Year") if istrue else print("Not Leap year")