N, M = map(int, input().split())
array1 = sorted(map(int, input().split()), reverse=False)
temp=0

while(True):
    for i in range(0, len(array1) - 2):
        if (array1[i]>M-2):
            continue
        else:
            for j in range(i+1, len(array1)-1):
                if (array1[i]+array1[j]>M-1):
                    continue
                else:
                    for k in range(j+1, len(array1)):
                        if (array1[i]+array1[j]+array1[k]>M):
                            continue
                        else:
                            if(array1[i]+array1[j]+array1[k]>temp):
                                temp=array1[i]+array1[j]+array1[k]
    print(temp)
    break