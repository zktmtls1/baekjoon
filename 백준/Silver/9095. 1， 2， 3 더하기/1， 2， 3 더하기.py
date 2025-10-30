N = 10
ARRY = [0] * (N + 1)
ARRY[1] =1
if(N>=2):
    ARRY[2] =2
if(N>=3):
    ARRY[3] =4
if(N>=4):
    for i in range(4, N+1):
        ARRY[i]= ARRY[i-1]+ ARRY[i-2]+ ARRY[i-3]

T=int(input())
for k in range(T):
    k=int(input())
    print(ARRY[k])


