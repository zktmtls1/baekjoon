import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip('\n') for _ in range(N)]       
arr.sort(key=lambda s: int(s.split()[0]))
print("\n".join(arr))
