n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(i+1) for i in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1,n):
    for j in range(i+1):
        left = dp[i-1][j-1] if j > 0 else 0
        right = dp[i-1][j] if j < i else 0

        dp[i][j] = max(left,right) + triangle[i][j]

print(max(dp[-1]))