import sys

MAXN = 123456
LIMIT = 2 * MAXN

is_prime = [False, False] + [True] * (LIMIT - 1)
p = 2
while p * p <= LIMIT:
    if is_prime[p]:
        for x in range(p * p, LIMIT + 1, p):
            is_prime[x] = False
    p += 1

pref = [0] * (LIMIT + 1)
for i in range(1, LIMIT + 1):
    pref[i] = pref[i - 1] + (1 if is_prime[i] else 0)

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    # (N, 2N] 의 소수 개수
    print(pref[2 * N] - pref[N])