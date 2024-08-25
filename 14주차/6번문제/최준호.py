from collections import deque

def solution(board):
    ox_cnt = {
        'O' : 0,
        'X' : 0
    }
    ox_win = {
        'O' : 0,
        'X' : 0
    }

    for i in range(3):
        ox_cnt['O'] += board[i].count('O')
        ox_cnt['X'] += board[i].count('X')
        if board[i] == board[i][0] * 3 and board[i][0] != '.':
            ox_win[board[i][0]] += 1
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            ox_win[board[0][i]] += 1

    if board[1][1] != '.':
        if board[0][0] == board[1][1] == board[2][2]:
            ox_win[board[0][0]] += 1
        if board[0][2] == board[1][1] == board[2][0]:
            ox_win[board[1][1]] += 1

    if ox_win['O'] and ox_win['X']:
        return 0
    if ox_win['O'] and ox_cnt['O'] <= ox_cnt['X']:
        return 0
    if ox_win['X'] and ox_cnt['O'] > ox_cnt['X']:
        return 0

    if ox_cnt['O'] - ox_cnt['X'] > 1 or ox_cnt['O'] - ox_cnt['X'] < 0:
        return 0

    return 1