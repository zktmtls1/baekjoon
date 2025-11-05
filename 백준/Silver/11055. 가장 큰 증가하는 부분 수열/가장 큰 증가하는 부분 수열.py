n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
for k in range(0, n):
    d[k]=arr[k]


for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] +arr[i])
print(max(d))