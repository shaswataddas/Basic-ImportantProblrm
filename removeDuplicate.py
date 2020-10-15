a = list(input())
a.sort()
i,j=0,1
p = len(a)
while j<p:
    if a[i]!=a[j]:
        i+=1
        j+=1
    else:
        a.remove(a[j])
        p-=1
print(a)