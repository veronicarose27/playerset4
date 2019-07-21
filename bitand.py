p=int(input())
u=list(map(int,input().split()))
m=u[0]
for i in range(1,p):
    m=m&u[i]
print (m)
