from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt():
    melt_list = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if iceberg[x][y] > 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<n and 0<=ny<m and iceberg[nx][ny] == 0:
                        melt_list[x][y]+=1
    for x in range(n):
        for y in range(m):
            iceberg[x][y] = max(iceberg[x][y]-melt_list[x][y], 0)



def count_chunks():

    visited = [[False]*m for _ in range(n)]
    chunks = 0
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
        while queue:   
            x,y = queue.popleft()                           
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and iceberg[nx][ny]>0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    for x in range(n):
        for y in range(m):
            if iceberg[x][y] >0 and not visited[x][y]:
                bfs(x,y)
                chunks+=1
    return chunks
    


years = 0
while True:
    chunks = count_chunks()
    if chunks >=2:
        print(years)
        break
    elif chunks == 0:
        print(0)
        break
    melt()
    years+=1