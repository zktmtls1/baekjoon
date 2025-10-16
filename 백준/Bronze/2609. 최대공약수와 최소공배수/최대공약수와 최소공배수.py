N1,N2 = map(int, input().split())
if(N1>N2):
    count = N1
else:
    count = N2

Min=1
Max=N1*N2

for i in range (count,1,-1):
    if((N1%i==0) and (N2%i==0)):
        N1//=i
        N2//=i
        Min*=i
        
print(Min)
print(Max//Min)