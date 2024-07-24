def solution(rows, columns, queries):
    
    answer = []

    matrix = [[i+(j*columns) for i in range(1, columns+1)] for j in range(rows)]

    def rotate_and_find_nums(q):
        x1, y1, x2, y2 = q[0], q[1], q[2], q[3]

        min_n = 10002

        # 가로-1 (x1,y1) ~ (x1,y2-1) -> (y에 +1씩.)
        nxt_v = matrix[x1-1 +1][y1-1]
        min_n = min(min_n, nxt_v)
        for y in range(y1-1, y2-1):
            tmp = matrix[x1-1][y]
            matrix[x1-1][y] = nxt_v
            nxt_v = tmp
            min_n = min(min_n, nxt_v)

        # 세로-1 (x1, y2) ~ (x2, y2) . (x에 +1씩.)
        for x in range(x1-1, x2):
            tmp = matrix[x][y2-1]
            matrix[x][y2-1] = nxt_v
            nxt_v = tmp
            min_n = min(min_n, nxt_v)

        # 가로-2 (x2, y2-1) ~ (x2, y1) <- (y에 -1씩)
        for y in range(y2-2, y1-2, -1):
            tmp = matrix[x2-1][y]
            matrix[x2-1][y] = nxt_v
            nxt_v = tmp
            min_n = min(min_n, nxt_v)

        # 세로-2 (x2-1, y1) ~ (x1-1, y1)
        for x in range(x2-2, x1-1, -1):
            tmp = matrix[x][y1-1]
            matrix[x][y1-1] = nxt_v
            nxt_v = tmp
            min_n = min(min_n, nxt_v)

        return min_n


    for q in queries:
        answer.append(rotate_and_find_nums(q))
    
    return answer