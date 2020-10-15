def checkPal(start,end,num):
    while start<end-1:
        if num[start]==num[end-1]:
            start+=1
            end-=1
        else:
            return 0
    return True

num = input()
end = len(num)
start = 0
istrue=checkPal(0,end,num)
print("YES") if istrue else print("NO")

