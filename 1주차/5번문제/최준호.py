from collections import deque

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(q):
    cnt = 0
    while q:
        x,y = q.popleft()

        if visited[x][y]:
            continue
        visited[x][y] = 1
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny]>0 and not visited[nx][ny]:
                q.append((nx,ny))

    return cnt

def initVisited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0

def setting(q):
    notEmpty = []
    while q:
        x,y = q.popleft()

        if visited[x][y]:
            continue
        visited[x][y] = 1

        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if board[nx][ny] <= 0:
                cnt += 1
            elif board[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx,ny))

        notEmpty.append((x,y,cnt))

    initVisited()
    return notEmpty


time = 1
while 1:
    q = deque([])
    for i in range(1,N):
        for j in range(1,M):
            if board[i][j] > 0:
                q.append((i,j))
                break
        if q:
            break

    notEmpty = setting(q)

    notMelt = 0
    s,e = 0,0
    for i,j,cnt in notEmpty:
        board[i][j] -= cnt
        if board[i][j] > 0:
            if not notMelt:
                s,e = i,j
            notMelt += 1

    if not s and not e:
        print(0)
        break

    if notMelt != check(deque([(s,e)])):
        print(time)
        break

    time += 1
    initVisited()




