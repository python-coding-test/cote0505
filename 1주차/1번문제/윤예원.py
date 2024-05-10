n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = maze[0][0]
for i in range(n):
    for j in range(m):
        #오른쪽으로 이동
        if j+1<m:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+maze[i][j+1])
        #아리로 이동
        if i+1<n:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+maze[i+1][j])
        #대각선 아래로 이동
        if i+1<n and j+1<m:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+maze[i+1][j+1])
print(dp[n-1][m-1])