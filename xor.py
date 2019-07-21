p=int(input())
q=list(map(int,input().split()))
l=q[0]
for i in range(1,p):
    l=l^q[i]
print(l)
