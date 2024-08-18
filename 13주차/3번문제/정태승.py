# 75.6/100 풀이입니다

def solution(maze):
    answer = 1010
    
    st_red, st_blue = None, None
    dst_red, dst_blue = None, None
    nxt_moves = [
        (0,1,0,1), (0,1,0,-1), (0,1,1,0), (0,1,-1,0),
        (1,0,0,1), (1,0,0,-1), (1,0,1,0), (1,0,-1,0),
        (0,-1,0,1), (0,-1,0,-1), (0,-1,1,0), (0,-1,-1,0),
        (-1,0,0,1), (-1,0,0,-1), (-1,0,1,0), (-1,0,-1,0)
    ]
    
    nxt_moves2 = [(0,1), (1,0), (-1,0), (0,-1)]

    
    N = len(maze)
    M = len(maze[0])
    
    # 초기화
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                st_red = (i,j)
            
            if maze[i][j] == 2:
                st_blue = (i,j)
            
            if maze[i][j] == 3:
                dst_red = (i,j)
            
            if maze[i][j] == 4:
                dst_blue = (i,j)
    
    
    def go(cur_red, cur_blue, vis_blue, vis_red, turns):
        if cur_red == dst_red and cur_blue == dst_blue:
            nonlocal answer
            answer = min(answer, turns)
            return
        
        red_x, red_y, blue_x, blue_y = cur_red[0], cur_red[1], cur_blue[0], cur_blue[1]
        
        if cur_red == dst_red :
            for d in nxt_moves2:
                nxt_blue_x = blue_x + d[0]
                nxt_blue_y = blue_y + d[1]
                
                if nxt_blue_x < 0 or nxt_blue_y < 0:
                    continue
                if nxt_blue_x >= N or nxt_blue_y >= M:
                    continue
                if maze[nxt_blue_x][nxt_blue_y]==5:
                    continue
                if (nxt_blue_x, nxt_blue_y) in vis_blue:
                    continue
                if (nxt_blue_x, nxt_blue_y) == cur_red:
                    continue
                vis_blue.append((nxt_blue_x, nxt_blue_y))
                go(cur_red, (nxt_blue_x, nxt_blue_y), vis_red, vis_blue, turns+1)
                vis_blue.pop()
                
        elif cur_blue == dst_blue :
            for d in nxt_moves2:
                nxt_red_x = red_x + d[0]
                nxt_red_y = red_y + d[1]
                
                if nxt_red_x < 0 or nxt_red_y < 0:
                    continue
                if nxt_red_x >= N or nxt_red_y >= M:
                    continue
                if maze[nxt_red_x][nxt_red_y]==5:
                    continue
                if (nxt_red_x, nxt_red_y) in vis_red:
                    continue
                if (nxt_red_x, nxt_red_y) == cur_blue:
                    continue
                vis_red.append((nxt_red_x, nxt_red_y))
                go((nxt_red_x, nxt_red_y), cur_blue, vis_red, vis_blue, turns+1)
                vis_red.pop()
        
        else:
            for d in nxt_moves:
                nxt_red_x = red_x + d[0]
                nxt_red_y = red_y + d[1]
                nxt_blue_x = blue_x + d[2]
                nxt_blue_y = blue_y + d[3]

                if nxt_red_x < 0 or nxt_red_y < 0 or nxt_blue_x < 0 or nxt_blue_y < 0:
                    continue
                if nxt_red_x >= N or nxt_red_y >= M or nxt_blue_x >= N or nxt_blue_y >= M:
                    continue
                if maze[nxt_red_x][nxt_red_y]==5 or maze[nxt_blue_x][nxt_blue_y]==5:
                    continue
                if (nxt_red_x, nxt_red_y) == (blue_x, blue_y) and (nxt_blue_x, nxt_blue_y) == (red_x, red_y):
                    continue # 수레끼리 자리 바꿔서 움직이기
                if (nxt_red_x, nxt_red_y) == (nxt_blue_x, nxt_blue_y): # 동시에 같은 칸 접근
                    continue
                if (nxt_red_x, nxt_red_y) in vis_red: # 이전에 방문한 칸인지 확인.
                    continue
                if (nxt_blue_x, nxt_blue_y) in vis_blue: # 이전에 방문한 칸인지 확인.
                    continue

                vis_red.append((nxt_red_x, nxt_red_y))
                vis_blue.append((nxt_blue_x, nxt_blue_y))
                go((nxt_red_x, nxt_red_y), (nxt_blue_x, nxt_blue_y), vis_red, vis_blue, turns+1)
                vis_red.pop()
                vis_blue.pop()
        
        
        return
    
    go(st_red, st_blue, [st_red], [st_blue], 0)
    
    return answer if answer!=1010 else 0