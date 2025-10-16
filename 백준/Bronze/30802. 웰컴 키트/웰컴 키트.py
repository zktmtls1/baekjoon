N= int(input())
array1 = list(map(int, input().split()))
T,P= map(int, input().split())

sum1=0
for i in range (len(array1)):
    if(array1[i]==0):
        continue
    else:
        sum1+=(1+(array1[i]-1)//T)

q= N//P
r= N%P

print(sum1)
print(f"{q} {r}")