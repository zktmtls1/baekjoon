N = int(input())
ARRY = [0] * (N + 1)
ARRY[1] =1
if(N>=2):
    ARRY[2] =3
if(N>=3):
    for i in range(3, N+1):
        ARRY[i]= ARRY[i-1]+ 2*ARRY[i-2]

print(ARRY[N]% 10007)