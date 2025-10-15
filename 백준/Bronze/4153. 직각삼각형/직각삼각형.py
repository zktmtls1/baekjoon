import sys
while(True):
    x,y,z = map(int, sys.stdin.readline().split())
    a, b, c = sorted([x, y, z])
    if((a==0) and (b==0) and (c==0)):
        break
    if(c*c==a*a+b*b):
        print("right")
    else:
        print("wrong")
        
