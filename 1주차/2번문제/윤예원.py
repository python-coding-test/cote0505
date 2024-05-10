n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]#인덱스 저장
index = 0
dp[0][0]= triangle[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0: #왼쪽 끝인 경우
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i: #오른쪽 끝
            dp[i][j] = dp[i-1][j-1] +triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+ triangle[i][j]

print(max(dp[n-1]))
