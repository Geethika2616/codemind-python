n=int(input())
s=n*n
t=0
g=0
while n>0:
    r=n%10
    t=t*10+r
    n=n//10
b=t**2
while b>0:
    v=b%10
    g=g*10+v
    b=b//10
print(g==s)