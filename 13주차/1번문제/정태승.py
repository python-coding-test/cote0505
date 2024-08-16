# 참고 https://velog.io/@seungjae/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-PCCP-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-2%EB%B2%88-%EC%84%9D%EC%9C%A0-%EC%8B%9C%EC%B6%94-Python-BFS
from collections import deque

def solution(land):
    M = len(land[0])
    N = len(land)
    res = [0 for _ in range(0,M)]
    answer = 0
    vis = {}
    for i in range(N): 
        for j in range(M): 
            if land[i][j] == 1 and (i, j) not in vis:
                min_y = j
                max_y = j
                petro = 0
                q = deque([(i,j)])
                vis[(i,j)] = True
                
                while q:
                    cx, cy = q.popleft()
                    petro += 1
                    min_y = min(min_y, cy)
                    max_y = max(max_y, cy)
                    
                    for d in [(0,1), (1,0), (-1,0), (0,-1)]:
                        nx = cx + d[0]
                        ny = cy + d[1]
                        
                        if nx < 0 or ny < 0 or nx >= N or ny >= M :
                            continue
                        if (nx, ny) in vis or land[nx][ny] == 0:
                            continue
                        
                        q.append((nx,ny))
                        vis[(nx,ny)] = True
                for k in range(min_y, max_y+1):
                    res[k] += petro
            

    return max(res)