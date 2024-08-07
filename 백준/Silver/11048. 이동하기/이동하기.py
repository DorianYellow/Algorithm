import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candy = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        candy[i][j] += max(candy[i - 1][j], candy[i][j - 1])
print(candy[n][m])
