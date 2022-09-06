n=int(input())
m=int(input())
pfs_n=0
for i in range(1,n):
    if n%i==0:
        pfs_n+=i
pfs_m=0
for i in range(1,m):
    if m%i==0:
        pfs_m+=i
if pfs_n==m and pfs_m==n:
    print("Amicable")
else:
    print("Not Amicable")