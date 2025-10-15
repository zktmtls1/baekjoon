
N=int(input())
i=0
total=1

while(True):
    total+=(i*6)
    i+=1
    if(total>=N):
        print(i)
        break