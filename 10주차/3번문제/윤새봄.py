def solution(rows, columns, queries):
    answer = []
    
    # rows x columns 크기인 행렬 생성.
    matrix = []
    for r in range(0, rows):
        matrix_row = []
        for c in range(1, columns+1):
            matrix_row.append(columns*r+c)
        matrix.append(matrix_row)
    # print(matrix)
    
    # 실패 코드
    # matrix_temp = copy.deepcopy(matrix)

    # for querie in queries:
    #     r1, c1, r2, c2 = querie[0], querie[1], querie[2], querie[3]
    #     min_value = rows*columns+1
    #     for r in range(r1-1, r2):
    #         for c in range(c1-1, c2):
    #             if (min_value > matrix[r][c]):
    #                 min_value = matrix[r][c]
    #             if (r >= r1-1 and r < r2-1 and c == c1-1):
    #                 rr = r+1
    #                 cc = c
    #             elif (r == r2-1 and c >= c1-1 and c < c2-1):
    #                 rr = r
    #                 cc = c+1
    #             elif (r > r1-1 and r <= r2-1 and c == c2-1):
    #                 rr = r-1
    #                 cc = c
    #             elif (r == r1-1 and c > c1-1 and c < c2):
    #                 rr = r
    #                 cc = c-1
    #             matrix[r][c] = matrix_temp[rr][cc]
    #     answer.append(min_value)  
    
    # 방향키 : 오른쪽 -> 아래 -> 왼쪽 -> 위 (시계방향 회전 흐름)
    dir_r = [0, 1, 0, -1]
    dir_c = [1, 0, -1, 0]
    
    for r1, c1, r2, c2 in queries:
        start_row = r1-1
        start_col = c1-1
        
        end_row = r2-1
        end_col = c2-1
        
        min_value = rows*columns+1
        direction = 0
        
        cur_row = start_row
        cur_col = start_col
        cur_value = matrix[cur_row][cur_col]      
        
        while(True):
            next_row = cur_row + dir_r[direction]
            next_col = cur_col + dir_c[direction]
            
            if (next_row < start_row or next_row > end_row or next_col < start_col or next_col > end_col):
                
                if (direction==3): # 시계방향으로 한 바퀴 다 돌은 것.
                    break
                
                direction += 1
                continue
                
            #print(f"cur_r, cur_c : ({cur_row}, {cur_col}) , next_r, next_c : ({next_row}, {next_col})")
            next_value = matrix[next_row][next_col]
            matrix[next_row][next_col] = cur_value
            
            if (cur_value < min_value):
                min_value= cur_value
            
            cur_value = next_value
            cur_row = next_row
            cur_col = next_col
            
        answer.append(min_value)
    
    return answer