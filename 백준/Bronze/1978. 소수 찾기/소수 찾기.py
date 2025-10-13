N = int(input())
array1 = []
array1 = list(map(int, input().split()))
count =0

for i in range (0,N):
    temp = array1[i]
    condition = True
    if (temp==1):
        condition = False
    elif (temp==2 or temp==3):
        condition = False
        count+=1
    for j in range (2,int(temp**0.5)+1):
        if(temp%j==0): 
            condition = False
            break
    if(condition):
        count +=1
print(count)