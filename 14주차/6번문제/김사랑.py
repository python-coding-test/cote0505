"""
실수인 상황
1. 승리 이후에도 표시가 되어있는 경우
    - 둘 다 승리한 경우
    - O가 승리, O의 개수가 X의 개수보다 2개 이상 많을 경우
    - X가 승리, O와 X의 개수가 다를 경우
2. "O"의 개수가 "X"보다 적거나, 2개 이상 많을 경우
"""

def solution(board):
    answer = 1
    cnt_o = 0
    cnt_x = 0
    n = len(board)
    
    for row in board:
        cnt_o += row.count("O")
        cnt_x += row.count("X")
    
    if cnt_o < cnt_x or cnt_o > cnt_x + 1:
        answer = 0
    
    def check_win(player):
        for col in range(n):
            if all(board[row][col] == player for row in range(n)):
                return True
        if all(board[i][i] == player for i in range(n)):
            return True
        if all(board[i][n-1-i] == player for i in range(n)):
            return True
        return False
    
    o_win = check_win('O')
    x_win = check_win('X')
    
    # 승리 이후 실수 검사
    if o_win and x_win:
        return 0
    if o_win and cnt_o != cnt_x + 1:
        return 0
    if x_win and cnt_o != cnt_x:
        return 0

    return answer
