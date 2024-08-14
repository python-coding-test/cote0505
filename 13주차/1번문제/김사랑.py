# 정확성 100%, 효율성 0%

from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_oil = 0
    
    def bfs(x, y, visited):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 1
        cnt = 1
    
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))  
        return cnt
    
    for i in range(m):
        visited = [[0 for _ in range(m)] for _ in range(n)]
        col_oil = 0
        for j in range(n):
            if land[j][i] == 1 and not visited[j][i]:
                col_oil += bfs(j, i, visited)
        
        # print(col_oil)
        max_oil = max(max_oil, col_oil)
        
    return max_oil
