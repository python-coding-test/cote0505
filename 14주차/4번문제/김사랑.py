from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    visited = set()
    results = []
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited.add((x, y))
        total_food = int(maps[x][y])
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] != 'X':
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    total_food += int(maps[nx][ny])
        
        return total_food
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and (i, j) not in visited:
                food_sum = bfs(i, j)
                results.append(food_sum)
    
    if not results:
        return [-1]
    
    return sorted(results)
