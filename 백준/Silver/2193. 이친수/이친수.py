n=int(input())
arry = [0] *(n+1)
arry[1] = 1

if(n>=2):
    arry[2] = 1
if(n>=3):
    for i in range (3,n+1):
        arry[i] = arry[i-1] + arry[i-2]

print(arry[n])
