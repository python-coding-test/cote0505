'''
석유 시추

세로 n 가로 m 격자 모양 땅 속 석유 발견
석유 여러 덩어리

시추관 수직 하남나



'''


land = 	[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]#[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

result = 9


from collections import deque

def solution(land):
    answer = []
    visited = [[0 for _ in range(len(land[0]))] for __ in range(len(land))]
    oil = [0] * len(land[0])
   

    def bfs(y,x):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        temp = set()
        cnt = 1
        queue = deque()
        queue.append([y,x])
        visited[y][x] = 1

        
        while queue:
            y,x = queue.popleft()
            temp.add(x)
            #print(x)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<=nx<len(land[0]) and 0<=ny<len(land) and land[ny][nx]==1 and not visited[ny][nx]:
                    queue.append([ny,nx])
                    visited[ny][nx] = 1
                    cnt+=1
        #print(temp)     
                    
                    
        
        
        for i in temp:
            oil[i] += cnt
        #print(cnt)
    

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i,j)

   
    
    return max(oil)


print(solution(land))
