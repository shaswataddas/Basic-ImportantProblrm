num = int(input())
isprime = True
for i in range(2,num):
    if num%i==0:
        isprime = False
if isprime:
    print("Prime")
else:
    print("Not Prime")
