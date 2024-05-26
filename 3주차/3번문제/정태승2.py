import sys

N, M = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline())

blocked = {}
for i in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split()) # (a,b), (c,d)
    blocked[(c, d, a, b)] = True
    blocked[(a, b, c, d)] = True

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N + 1):
    for j in range(M + 1):
        if i < N and (i, j, i + 1, j) not in blocked:
            dp[i + 1][j] += dp[i][j]
        if j < M and (i, j, i, j + 1) not in blocked:
            dp[i][j + 1] += dp[i][j]

print(dp[N][M])