def fac(n):
    if n < 0:
        return
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

N,K= map(int, input().split())
print(int(fac(N)/fac(K)/fac(N-K)))