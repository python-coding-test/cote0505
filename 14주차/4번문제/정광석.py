'''
무인도 여행 지도보기
지도에 바다, 무인도 정보 표시

1 * 1 사각형 이루어짐
X 1,~9 자연수, X : 바다   숫자 : 무인도

상하좌우 연결되는 땅은 하나의 무인도

각 칸의 숫자 : 식량
상하좌우 모두 더한 값 : 해당 섬에서 얼마나 머무를 수 있는가?


'''
maps,	result=["XXX","XXX","XXX"],0#["X591X","X1X5X","X231X", "1XXX1"],	[1, 1, 27]
from collections import deque

def solution(maps):
    answer = []

    n, m = len(maps), len(maps[0]) # n: 4, m : 5
    visited = [[0 for _ in range(m)] for __ in range(n)]
    #print(visited)
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    
    def bfs(y,x):
        
        queue = deque()
        queue.append([y,x])
        visited[y][x] = 1
        days = 0

        while queue:
            ty,tx = queue.popleft()
            days+=int(maps[ty][tx])
            for i in range(4):
                ny,nx = ty+dy[i], tx+dx[i]
                
                if 0<=ny<n and 0<=nx<m:
                    if visited[ny][nx] : continue
                    if maps[ny][nx] == 'X': continue
                    
                    queue.append([ny,nx])
                    visited[ny][nx] = 1
                    #print(ny,nx)
        answer.append(days)


    for i in range(n):
        for j in range(m):
            if maps[i][j] !='X' and visited[i][j]==0:
                bfs(i,j)
    

    if len(answer)==0:
        answer = [-1]

    answer.sort()
    return answer


print(solution(maps))