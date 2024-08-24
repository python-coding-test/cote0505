from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def solution(maps):
    answer = []

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        food = 0

        while q:
            x, y = q.popleft()

            if maps[x][y] == 'X':
                continue

            food += int(maps[x][y])
            maps_temp = list(maps[x])
            maps_temp[y] = 'X'
            maps[x] = ''.join(maps_temp)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                    q.append((nx, ny))

        return food

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                foodSum = bfs(i, j)
                answer.append(foodSum)

    answer.sort()

    if not answer:
        return [-1]

    return answer