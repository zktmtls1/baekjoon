n=int(input())
arry = [[0] * 10 for _ in range(n+1)]

for i in range (0,10):
    arry[1][i] = 1

for j in range (2,n+1): #길이 n까지
    for k in range (0,10): #각 자리수별
        for l in range (0,k+1): #이하 자리수
            arry[j][k] += arry[j-1][l]
sum1=0

for a in range(0,10):
    sum1 +=arry[n][a]
print(sum1%10007)
