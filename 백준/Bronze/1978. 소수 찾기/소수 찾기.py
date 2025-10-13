N = int(input())
nums = list(map(int, input().split()))
count = 0

for x in nums:
    if x < 2:
        continue
    j = 2
    while j * j <= x:
        if x % j == 0:
            break
        j += 1
    else:
        count += 1

print(count)