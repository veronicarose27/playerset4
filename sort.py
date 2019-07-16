p=int(input())
word=list(map(str,input().split()[:p]))
word.sort()
word.sort(key=len)
for i in word:
    print(i,end=" ")
