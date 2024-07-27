'''
1 부터 써진 행렬

직사각형 범위 여러번 선택해서

테두리 숫자 시계방향 회전

회전 시킨 것 중 가장 작은 수를 리스트에 넣기


'''

rows = 6
columns = 7
queries =[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):

    board = [[i+j*columns for i in range(1,columns+1,1)] for j in range(rows)]
    answer = []
    #print(board)
    def check(x1,y1,x2,y2):
        temp = board[x1-1][y1-1]
        min_num = temp

        for k in range(x1-1,x2-1):
            test = board[k+1][y1-1]
            board[k][y1-1] = test
            min_num = min(min_num, test)

        for y in range(y1-1,y2-1):
            test = board[x2-1][y+1]
            board[x2-1][y] = test
            min_num = min(min_num, test)

        for k in range(x2-1,x1-1,-1):
            test = board[k-1][y2-1]
            board[k][y2-1] = test
            min_num = min(min_num, test)

        for y in range(y2-1,y1-1,-1):
            test = board[x1-1][y-1]
            board[x1-1][y] = test
            min_num = min(min_num, test)
        
        board[x1-1][y1] = temp
        #print(board)
        return min_num 
                     
        

    for q in queries:
        x1,y1,x2,y2 = q
        answer.append(check(x1,y1,x2,y2))
    return answer



print(solution(rows,columns, queries))
