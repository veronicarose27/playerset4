a,x,z=map(int,input().split())
if(a!=0 and x!=0 and z!=0):
    an=a+x+z
else:
    an=0
if(an==180):
    print("yes")
else:
    print("no")
