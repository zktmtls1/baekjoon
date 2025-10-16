N=int(input())
array1 = sorted(map(int, input().split()), reverse=True)
result=0

for i in range (N):
    result+=array1[i]/array1[0]*100
print(result/N)