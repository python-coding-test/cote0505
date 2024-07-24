# 틀린풀이입니다.
# 정답 풀이는 : https://blog.encrypted.gg/1032
# 실제 풀이는 minimax tree를 이용해야한다 합니다.


# 60'
import sys
sys.setrecursionlimit(10**5)

def solution(board, aloc, bloc):
    answer = float('inf')
    R = len(board)
    C = len(board[0])
    
    # 만약 두 플레이어 위치가 같다면
    if aloc == bloc:
        return 0
        
    
    def go(turn, p1x, p1y, p2x, p2y):
        nonlocal answer
        
        if turn%2 == 0 : # player1의 턴 (player A)
            cx, cy = p1x, p1y
        else: # player2의 턴 (player B)
            cx, cy = p2x, p2y
        
        # 현재 밟고 있는 발판이 없어졌다면 종료
        if board[cx][cy] == 0:
            answer = min(answer, turn)
            return
            
        
        can_go_paths = []
        
        # 현재 플레이어 위치에서 갈 수 있는 곳 확인.
        for d in [(0,1), (0,-1), (1, 0), (-1,0)]:
            nx = cx + d[0]
            ny = cy + d[1]
            
            if nx >= R or ny >= C or nx < 0 or ny < 0:
                continue
                
            if board[nx][ny] == 0 :
                continue
            
            can_go_paths.append((nx, ny))

        # 현재 플레이어가 갈 수 있는 곳이 없다면.
        if not can_go_paths:
            answer = min(answer, turn)
            return
        
        # 현재 플레이어가 갈 수 있는 곳이 있다면,
        if turn%2 == 0: # p1인 경우,
            # 현재 플레이어가 갈 수 있는 곳이 다른 플레이어가 밟은 발판 이외의 공간이 존재하는 경우,
            if (p2x, p2y) in can_go_paths and len(can_go_paths) >= 2: 
                # 해당 점 제외하고 이동하기.
                for path in can_go_paths:
                    if (p2x, p2y) == path:
                        continue
                    board[cx][cy] = 0 
                    go(turn+1, path[0], path[1], p2x, p2y)
                    board[cx][cy] = 1
            else :
                for path in can_go_paths:
                    board[cx][cy] = 0
                    go(turn+1, path[0], path[1], p2x, p2y)
                    board[cx][cy] = 1
        
        else : # p2인 경우,
            if (p1x, p1y) in can_go_paths and len(can_go_paths) >= 2: 
                # 해당 점 제외하고 이동하기.
                for path in can_go_paths:
                    if (p1x, p1y) == path:
                        continue
                    board[cx][cy] = 0 
                    go(turn+1, p1x, p1y, path[0], path[1])
                    board[cx][cy] = 1
            else :
                for path in can_go_paths:
                    board[cx][cy] = 0
                    go(turn+1, p1x, p1y, path[0], path[1])
                    board[cx][cy] = 1
        return
    
    go(0, aloc[0], aloc[1], bloc[0], bloc[1])

    return answer

# 로직 : turn 수가 가장 짧고, 모든 플레이어들은 가능한 다른 플레이어의 발판쪽으로 가지 않는다.
