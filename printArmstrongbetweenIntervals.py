def checkArm(num):
    mysum=0
    for i in num:
        mysum+=int(i)**3
    return 1 if int(num)==mysum else 0

start = int(input("Lower Range: "))
end = int(input("Upper Range: "))
for k in range(start,end+1):
    isam = checkArm(str(k))
    print(k) if isam else 0