dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(me,opp, board):
    x,y = me
    if not board[x][y]:
        return 0

    max_res = 0
    min_res = float('inf')
    isWin = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == 1:
            board[x][y] = 0
            step = dfs(opp, (nx,ny), board) + 1
            board[x][y] = 1

            if step % 2:
                isWin = 1
                min_res = min_res if min_res<step else step
            else:
                max_res = max_res if max_res>step else step

    if isWin:
        return min_res
    else:
        return max_res


def solution(board, aloc, bloc):
    answer = dfs(aloc, bloc, board)
    return answer
