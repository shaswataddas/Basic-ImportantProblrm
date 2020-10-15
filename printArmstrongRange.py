def checkArm(num):
    mysum=0
    for i in num:
        mysum+=int(i)**3
    return 1 if int(num)==mysum else 0

ran = int(input())
for k in range(0,ran+1):
    isam = checkArm(str(k))
    print(k) if isam else 0