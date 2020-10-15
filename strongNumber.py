def checkStrong(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

num = input()
s=0
for i in num:
    s = checkStrong(int(i))+s
print("Strong Number") if s==int(num) else print("Not")
print(s,num)