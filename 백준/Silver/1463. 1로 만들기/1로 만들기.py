N = int(input())
ARRY = [0] * (N + 1)

for i in range(1, N):
    ARRY[i+1]= ARRY[i]+1
    if (i + 1) % 2 == 0:
        ARRY[i+1] = min(ARRY[i+1], ARRY[(i+1)//2] + 1)
    if (i + 1) % 3 == 0:
        ARRY[i+1] = min(ARRY[i+1], ARRY[(i+1)//3] + 1)

print(ARRY[N])