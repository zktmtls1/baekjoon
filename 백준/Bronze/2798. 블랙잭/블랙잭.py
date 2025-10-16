import sys

N, M = map(int, input().split())
array1 = sorted(map(int, input().split()))
temp = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s = array1[i] + array1[j] + array1[k]
            if s == M:
                print(M)
                sys.exit(0)   # 전체 종료
            if s < M and s > temp:
                temp = s
print(temp)