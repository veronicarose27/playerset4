p=int(input())
u=list(map(int,input().split()))
l=[]
m=u[0]
for i in range(1,p):
    m=m|u[i]
    l.append(m)
print (max(l))
