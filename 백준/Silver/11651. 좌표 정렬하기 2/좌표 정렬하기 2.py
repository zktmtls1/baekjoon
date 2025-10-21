import sys
input = sys.stdin.readline

N = int(input())
arr = [str(input()).rstrip("\n") for n in range(N)]
arr.sort(key=lambda s: (int(s.split()[1]), int(s.split()[0])))
print("\n".join(arr))