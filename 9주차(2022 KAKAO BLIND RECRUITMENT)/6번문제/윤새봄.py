def solution(board, skill):
    answer = 0
    # 효율성 테스트를 통과하려면, 누적합 개념으로 접근해야 함.
    temp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    # print(temp)
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # 적의 공격일 때
            degree = degree * (-1)
        # 누적합 적용 - 행에 대해 
        temp[r1][c1] += degree
        temp[r1][c2+1] += degree * (-1)
        # 누적합 적용 - 열에 대해
        temp[r2+1][c1] += degree * (-1)
        temp[r2+1][c2+1] += degree
        
    # 행에 대해 누적합 적용
    for r in range(len(temp)-1):
        for c in range(len(temp[0])-1):
            temp[r][c+1] += temp[r][c]   
    
    # 열에 대해 누적합 적용
    for c in range(len(temp[0])-1):
        for r in range(len(temp)-1):
            temp[r+1][c] += temp[r][c]
    
    # 기존 board에 temp 합치기.
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += temp[r][c]
            if(board[r][c]>0):
                answer += 1
    
    return answer