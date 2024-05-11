import sys
input = sys.stdin.readline
n = int(input())
rock = list(map(int, input().split()))
dp = [0]*n
min_val = float("inf")
for i in range(n):
    dp[i] = max((i)*(1+abs(rock[0]-rock[i])),(4-i)*(1+abs(rock[4]-rock[i])))
    min_val = min(dp[i], min_val)
print(min_val)