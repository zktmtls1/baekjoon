N=int(input())
start = max(0, N - 9 * len(str(N)))

for i in range(start,N):
    temp = sum(map(int, str(i)))
    if(N==i+temp):
        print(i)
        break
else: 
    print(0)