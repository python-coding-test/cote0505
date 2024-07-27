def solution(rows, columns, queries):
    arr = [[0]*columns for _ in range(rows)]  # 2차원 배열 초기화
    cnt = 1
    result = []

    # 배열에 초기 값 설정
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1
    
    for r1, c1, r2, c2 in queries:
        min_v = 10001
        before = arr[r1][c1-1]  # 회전의 시작점 값을 before에 저장

        # 위쪽 회전
        for i in range(c1-1, c2):
            min_v = min(arr[r1-1][i], min_v)  # 최소값 갱신
            before, arr[r1-1][i] = arr[r1-1][i], before  # 값 교환

        # 오른쪽 회전
        for i in range(r1, r2):
            min_v = min(arr[i][c2-1], min_v)  # 최소값 갱신
            before, arr[i][c2-1] = arr[i][c2-1], before  # 값 교환

        # 아래쪽 회전
        for i in range(c2-2, c1-2, -1):
            min_v = min(arr[r2-1][i], min_v)  # 최소값 갱신
            before, arr[r2-1][i] = arr[r2-1][i], before  # 값 교환

        # 왼쪽 회전
        for i in range(r2-2, r1-1, -1):
            min_v = min(arr[i][c1-1], min_v)  # 최소값 갱신
            before, arr[i][c1-1] = arr[i][c1-1], before  # 값 교환

        result.append(min_v)  # 현재 회전에서의 최소값을 결과에 추가

    return result
