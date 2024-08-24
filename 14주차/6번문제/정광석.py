'''
틱택토

3*3 빈칸 게임판 선공 O 후공 X 번갈아 빈칸에 표시
가로세로대각선 3개 같은 표시 만들면 승리 , 게임 종료
9칸 다차면 무승부

혼자 틱택토
혼자 선후공

수십판했더니 실수 했을 수도
O 할 차롄데 X 표시 혹은 반대로
선공이나 후공이 승리해서 게임이 종료 됬는데도 진행


실수 했는지 의문이 생김
이를 알 수는 없음

게임판을 봤을 때 규칙을 지켜서 진행했을 때 나올 수 있는 상황인지 체크


'''

board	,result = ["OOO", "...", "XXX"],1#["O.X", ".O.", "..X"]	,1

def solution(board):
    answer = 1
    # 가로 세로는 
   
    
    def win(winner):
        for i in range(3):
            
            if board[i] == winner*3:
                return True
            
            if board[0][i] == board[1][i] == board[2][i] == winner:
                return True


        if board[0][0] == board[1][1] == board[2][2] == winner:
            return True
        if board[0][2]  == board[1][1] == board[2][0] == winner:
            return True
        return False

    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt+=1
            elif board[i][j] == 'X':
                x_cnt+=1


    # 표시를 바꿔서 하는 경우
    if o_cnt < x_cnt or o_cnt > x_cnt + 1:
        return 0 #후공이 더 많이 두는 경우 불가능, O가 2개이상 많아도 불가능
  
    # 한명이 이겼는데 계속한 경우
    if win('O') and win('X'):
        return 0
    # 선공이 이겼는데 O개수가 X개수보다 1많지 않은 경우
    if win('O') and o_cnt != x_cnt+1:
        return 0
    # 후공이 이겼는데 O개수가 X개수랑 같지 않은 경우
    if win('X') and o_cnt != x_cnt:
        return 0
    
    
    
    
    
    

    return answer

print(solution(board))