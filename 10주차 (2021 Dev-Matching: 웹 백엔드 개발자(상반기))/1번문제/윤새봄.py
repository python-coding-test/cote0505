def solution(board, aloc, bloc):
    answer = -1
    
    # 위, 아래, 오른쪽, 왼쪽
    dir_r = [-1, 1, 0, 0]
    dir_c = [0, 0, 1, -1]    
        
    def is_blocked(board, r, c):    
        for d in range(4):
            next_r = r + dir_r[d]
            next_c = c + dir_c[d]
            if (next_r >= 0 and next_r < len(board) and next_c >= 0 and next_c < len(board[0])):
                if (board[next_r][next_c]==1):
                    return False
        return True
                
    def dfs(board, r1, c1, r2, c2):
        if is_blocked(board, r1, c1): # 이동할 곳이 없을 때, 해당 플레이어 패배.
            return [False, 0]
        
        if (r1 == r2 and c1 == c2): # A와 B가 같은 자리에 있는 것. 무조건 (r1,c1)에 있는 해당 플레이어가 이김.
            return [True, 1]
        
        min_value = 987654321
        max_value = 0
        can_win = False
        
        for d in range(4):
            next_r = r1 + dir_r[d]
            next_c = c1 + dir_c[d]
            if (next_r < 0 or next_r >= len(board) or next_c < 0 or next_c >= len(board[0])):
                continue
            if (board[next_r][next_c]==0):
                continue
            # print(f" (r1, c1) : ({r1},{c1})")    
            board[r1][c1] = 0
            result = dfs(board, r2, c2, next_r, next_c)
            board[r1][c1] = 1
            
            if (result[0] == False): # 상대 플레이어가 지고, 해당 플레이거 이김. 해당 플레이어는 빨리 승기하기 위해, min_value를 찾는다.
                can_win = True
                min_value = min(min_value, result[1])
            else: # 상대 플레이어가 이기고, 해당 플레이어가 짐. 해당 플레이어는 최대한 오래 버티기 위해, max_value를 찾는다.
                 max_value = max(max_value, result[1])
        
        if (can_win):
            turn = min_value
        else:
            turn = max_value
            
        return [can_win, turn + 1]
    
    answer = dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]
    
    return answer