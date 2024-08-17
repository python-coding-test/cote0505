'''
n m 짜리 격자 퍼즐판


빨강 파랑 수레 하나씩, 
각 수레는 시작칸에서 부터 도착칸 까지 이동해야 함


각 턴 마다 반드시 모든 수레를 상하 좌우로 인접한 칸 중 하나로

벽, 격자 밖 못감
갔던 곳 못감
도착했으면 움직이지 않음
동시에 두 수레를 같은 칸 움직일 수 없음
수레끼리 자리 바꾸며 어ㅜㅁ직일 수  없음



'''
maze = 	[[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]
# 실패// 일부 예제 실패 이유 잘 모르음


from collections import deque

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    # 수레의 시작 위치와 목표 위치를 찾기
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)
    
   
    queue = deque([(red_start, blue_start, 0)])
    visited = set((red_start, blue_start))

    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        (red_pos, blue_pos, steps) = queue.popleft()
        red_y, red_x = red_pos
        blue_y, blue_x = blue_pos
        
        # 모두 도착
        if red_pos == red_end and blue_pos == blue_end:
            return steps
        
        
        for d1 in directions:
            new_red_y, new_red_x = red_y + d1[0], red_x + d1[1]
            
            
            if 0 <= new_red_y < n and 0 <= new_red_x < m and maze[new_red_y][new_red_x] != 5:
                new_red_pos = (new_red_y, new_red_x)
                
               
                if new_red_pos == red_end:
                    new_red_pos = red_end
            else:
                new_red_pos = red_pos  # 못 가
            
            for d2 in directions:
                new_blue_y, new_blue_x = blue_y + d2[0], blue_x + d2[1]
                
                
                if 0 <= new_blue_y < n and 0 <= new_blue_x < m and maze[new_blue_y][new_blue_x] != 5:
                    new_blue_pos = (new_blue_y, new_blue_x)
                    
                    
                    if new_blue_pos == blue_end:
                        new_blue_pos = blue_end
                else:
                    new_blue_pos = blue_pos  
                
                # 두 수레가 같은 칸에 도달할 수 없음
                if new_red_pos == new_blue_pos or (new_red_pos, new_blue_pos)  in visited: continue # 겹침 제외
                    
                if not (new_red_pos == blue_pos and new_blue_pos == red_pos): # 자리교환 제외
                    visited.add((new_red_pos, new_blue_pos))
                    queue.append((new_red_pos, new_blue_pos, steps + 1))

    return 0  


print(solution(maze))  
