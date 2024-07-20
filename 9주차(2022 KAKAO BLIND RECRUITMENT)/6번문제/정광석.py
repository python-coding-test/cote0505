'''
N M 행렬 크기 맵
내구도 건물 칸마다 하나씩



'''

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]

skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

# 효율성 테스트 불합격
def solution(board, skill):
    answer = 0
    cal = [[0 for i in range(len(board[0]))]] * len(board)
    
    for s in skill:
        r0,c0,r1,c1,change = s[1:]
        
        if s[0]==1:
            # 공격
            for j in range(r0,r1+1,1):
                for i in range(c0, c1+1,1):
                    board[j][i]-=change
        else:
            # 수리
            for j in range(r0,r1+1,1):
                for i in range(c0, c1+1,1):
                    board[j][i]+=change

    for r in board:
        answer += len(list(filter(lambda x : x>0, r)))

    return answer

print(solution(board, skill))

