import math
pl=int(input())
pl=math.radians(pl)
print(pl)
if (pl>0 and pl<1):
    print(round(math.sin(pl),2))
else:
    print(round(math.sin(pl)))  
