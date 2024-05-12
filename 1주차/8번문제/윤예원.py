INF = 999999999
import sys
input = sys.stdin.readline
n = int(input())
rock = list(map(int, input().split()))
dp = [0] + [INF]*(n-1)
for i in range(1,n):
    for j in range(0, i):
        min_val = max((i-j)*(1+abs(rock[j]-rock[i])),dp[j])
        dp[i] = min(dp[i], min_val)
print(dp[-1])