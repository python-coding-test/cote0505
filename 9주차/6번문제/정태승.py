



# 1번 풀이 (틀림)
# # 4'10''
# def solution(board, skill):
#     answer = 0
#     N = len(board[0])
#     M = len(board)
#     cal = [-1, 1]
#     dead_buildings = {}
    
#     for s in skill:
#         for r in range(s[1], s[3]+1):
#             for c in range(s[2], s[4]+1):
#                 degree = (s[5]*cal[s[0]-1])
#                 board[r][c]+=degree
#                 if board[r][c] <= 0:
#                     dead_buildings[(r, c)] = True
    
#     dead = 0
#     for d in dead_buildings.keys():
#         if board[d[0]][d[1]] <= 0:
#             dead+=1
    
#     return N*M-dead

# 2번 풀이 (누적합)
def solution(board, skill):
    answer = 0
    tmp=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]# 누적합 기록을 위한 배열
    
    for t, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1]+=degree if t == 2 else -degree
        tmp[r1][c2+1]+=-degree if t == 2 else degree
        tmp[r2+1][c1]+=-degree if t == 2 else degree
        tmp[r2+1][c2+1]+=degree if t == 2 else -degree
        
    # 행 기준 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1]+= tmp[i][j]

    # 열 기준 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j]  += tmp[i][j]
            
    # 기존 배열과 합함
    for i in range(len(board)):
          for j in range(len(board[i])):
                board[i][j]+=tmp[i][j]
                if board[i][j] > 0:
                      answer+=1
    return answer