import sys
input = sys.stdin.readline

MOD = 1000000007

def pow_base(x):
    check = bin(x)[2:]
    length = len(check)

    arr = []
    for i in range(length):
        if check[i] == '1':
            arr.append(length - i - 1)
    return arr

def pow(x, n):
    for _ in range(n):
        x = (x ** 2) % MOD
    return x

def mod_inv(x, arr):
    ans = 1
    for i in arr:
        ans *= pow(x, i)
        ans %= MOD
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    mod_arr = pow_base(MOD - 2)
    ans = 1
    tmp = 1
    for i in pow_base(m):
        tmp *= pow(n, i)
        tmp %= MOD
    ans *= (tmp - 1)
    ans %= MOD
    ans *= mod_inv(n - 1, mod_arr)
    ans %= MOD
    print(ans)