upto = int(input())
for j in range(2,upto+1):
    isprime = True
    for i in range(2,j):
        if j%i==0:
            isprime = False
    print(j) if isprime else 0