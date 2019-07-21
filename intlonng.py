n2=int(input())
if(n2>=-2**15+1)and(n2<=2**15+1):
    print("INT")
elif(n2>=-2**31+1)and(n2<=2**31+1):
    print("LONG")
else:
    print("LONG LONG")


