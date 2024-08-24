def solution(maps):
    answer = []
    
    dir_r = [-1, 0, 1, 0]
    dir_c = [0, 1, 0, -1]
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c]!="X" and visited[r][c]!=1:
                period=0
                q = [(r,c)]
                
                while q:
                    rr, cc = q.pop()
                    if (visited[rr][cc]==1):
                        continue
                    visited[rr][cc]=1
                    period += int(maps[rr][cc])
                    #print(f"rr: {rr}, cc: {cc}")
                    #print(f"period :{period}")
                    for d in range(4):
                        next_r, next_c = rr+dir_r[d], cc+dir_c[d]
                        if (0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]) and maps[next_r][next_c] != 'X' and visited[next_r][next_c]==0):
                            q.append((next_r, next_c))
                
                answer.append(period)
                        
    if answer:
        answer.sort()
    else:
        answer = [-1]
    
    return answer