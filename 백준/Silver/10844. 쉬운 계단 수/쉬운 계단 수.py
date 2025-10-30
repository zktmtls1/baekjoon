n=int(input())
arry = [[0] * 10 for _ in range(n+1)]

for i in range (1,10):
    arry[1][i] = 1

for j in range (2,n+1):
    arry[j][0] = arry[j-1][1] 
    arry[j][1] = arry[j-1][0] +arry[j-1][2]
    arry[j][2] = arry[j-1][1] +arry[j-1][3]
    arry[j][3] = arry[j-1][2] +arry[j-1][4]
    arry[j][4] = arry[j-1][3] +arry[j-1][5]
    arry[j][5] = arry[j-1][4] +arry[j-1][6]
    arry[j][6] = arry[j-1][5] +arry[j-1][7]
    arry[j][7] = arry[j-1][6] +arry[j-1][8]
    arry[j][8] = arry[j-1][7] +arry[j-1][9]
    arry[j][9] = arry[j-1][8]

sum1=0
for k in range(0,10):
    sum1 +=arry[n][k]
print(sum1%1000000000)