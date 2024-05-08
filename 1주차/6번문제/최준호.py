import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]

    print(dp[M])