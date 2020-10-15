#GCD of two Number.

a = int(input("Enter a number: "))
b = int(input("Second number: "))
result = 1
a = min(a,b)
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        result = i
        break
print(result) 