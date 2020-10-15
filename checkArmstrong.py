num = input()
mysum=0
for i in num:
    mysum+=int(i)**3
print("Armstrong") if int(num)==mysum else print("No")
print(mysum,num)