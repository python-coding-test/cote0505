import sys
input = sys.stdin.readline
INF =  999999999
n,k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] + [INF]* (n-1)
for i in range(1,n):
    for j in range(i):
        val = arr[i]-arr[j]
        min_val = max((i-j)*(1+abs(val)), dp[j])
        dp[i] = min(min_val, dp[i])
if dp[-1] <= k:
    print("YES")
else: 
    print("NO")