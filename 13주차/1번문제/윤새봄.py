from collections import deque
def solution(land):
    answer = 0
    
    dir_r = [0, -1, 0, 1]
    dir_c = [-1, 0, 1, 0]
    
    visited = [[0 for j in range(len(land[0]))] for i in range(len(land))]
    #print(visited)
    result = [0 for i in range(len(land[0]))]
    #print(result)
    
    def bfs(r, c):
        visited[r][c] = 1
        q = deque()
        q.append((r,c))
        count = 0
        min_col, max_col = c, c
        while q:
            row, col = q.popleft()
            count += 1
            for d in range(4):
                next_row = row + dir_r[d]
                next_col = col + dir_c[d]
                if (next_row < 0 or next_row >= len(land) or next_col < 0 or next_col >= len(land[0])):
                    continue
                if (visited[next_row][next_col]==0 and land[next_row][next_col]==1):
                    visited[next_row][next_col]=1
                    min_col = min(min_col, next_col)
                    max_col = max(max_col, next_col)
                    q.append((next_row, next_col))
        
        for rr in range(min_col, max_col+1):
            result[rr]+=count
    
    for r in range(len(land)):
        for c in range(len(land[0])):
            if (visited[r][c]==0 and land[r][c]==1):
                bfs(r,c)
    
    answer = max(result)
    
    return answer