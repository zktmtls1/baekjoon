import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    a, b = map(int, input().split(','))
    out.append(str(a + b))
print("\n".join(out))