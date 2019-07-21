n4=int(input())
l=[int(i) for i in input().split()]
r4=0
for i in range(0,n4):
    for j in range(i+1,n4):
        r4=l[i]^l[j]
print(r4)
