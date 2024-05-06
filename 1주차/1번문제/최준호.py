from collections import deque

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,-1,0]
dy = [-1,0,-1]
dp = [[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        temp = [0]
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <N and 0<= ny <M:
                temp.append(dp[nx][ny])
        dp[x][y] = max(temp) + board[x][y]
print(dp[N-1][M-1])