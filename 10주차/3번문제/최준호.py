from collections import deque

def rotation(arr, query, answer):
    sx,sy,ex,ey = query
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    l = ex - sx
    w = ey - sy

    q = deque(arr[sx][sy:ey+1])
    for i in range(l):
        q.append(arr[sx+i+1][ey])
    for i in range(w):
        q.append(arr[ex][ey-i-1])
    for i in range(l-1):
        q.append(arr[ex-i-1][sy])

    minNum = min(q)
    answer.append(minNum)

    # 바꾸기
    for i in range(w):
        arr[sx][sy+1+i] = q.popleft()
    for i in range(l):
        arr[sx+i+1][ey] = q.popleft()
    for i in range(w):
        arr[ex][ey-i-1] = q.popleft()
    for i in range(l):
        arr[ex-i-1][sy] = q.popleft()

    return arr, answer

def solution(rows, columns, queries):
    answer = []

    cnt = 0
    arr = [[]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(cnt+1,columns+cnt+1):
            arr[i].append(j)
        cnt += columns

    for query in queries:
        rotation(arr, query,answer)

    return answer