'''
로봇이 움직이는 방법

가로 1칸 이동
세로 1칸 이동

회전
- 왼/오/위/아래 축 잡고 이동

왼쪽 가로 이동
x1, y1, x2, y2 -> x1, y1-1, x2, y2-1

오른쪽 가로 이동
x1, y1, x2, y2 -> x1, y1+1, x2, y2+1

아래 세로 이동
x1, y1, x2, y2 -> x1+1, y1, x2+1, y2

위 세로 이동
x1, y1, x2, y2 -> x1-1, y1, x2-1, y2

가로 회전 이동 (s1 축 위 아래 )

x1, y1, x2, y2 -> x1, y1, x1-1, y1
                  x1, y1, x1+1, y1

s2 축 위아래

x1, y1, x2, y2 -> x2, y1, x2, y2
                  x1, y1, x2, y2
                  

총 12가지 케이스


'''


# 책 코드 카피 


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

result = 7

gdx = []
gdy = []

from collections import deque

def solution(board):
    answer = 0 # 최소 시간 구하기
    def get_next_pos(pos, board):
        next_pos = []
        pos = list(pos)
        pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

            if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
                next_pos.append({(pos1_next_x, pos1_next_y),(pos2_next_x, pos2_next_y)})

            if pos1_x == pos2_x: #가로로 놓인 경우
                for i in [-1,1]:
                    if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                        next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                        next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
            
            elif pos1_y == pos2_y:
                for i in [-1,1]:
                    if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                        next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                        next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
        return next_pos

    n = len(board)

    q = deque()
    visited = []
    pos = {(1,1),(1,2)}


    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q.append((pos, 0))
    visited.append(pos)




    while q:
        pos, cost = q.popleft()

        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):

            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)



    
   





    return answer


print(solution(board))