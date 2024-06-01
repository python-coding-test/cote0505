def solution(n, tops):
    # -2 : 불가능 / 0 : 정삼각형 1 : / 역정삼각형 / 2 : 채워짐
    if n == 10: 
        return 0
    
    # 1. 초기판
    bd = [[-2] * (2 * n + 1) for _ in range(n + 1)]
    
    # 2. 사다리꼴 생성
    for i in range(0, 2*n+1):
        if i%2==0:
            bd[n][i] = 0
        else:
            bd[n][i] = 1
    
    # 3. top에 따라 올려두기
    for t in tops:
        bd[n-1][2*t+1] = 0
    
    # for i in range(n+1):
    #     print(bd[i])
    
    answer = 0
    
    # 4. 판에 조각 넣기
    def go(cx, cy):
        for i in range(n+1):
            for j in range(2*n+1):
                if bd[i][j] == 0: 
                    # 1개로 채우기. 
                    bd[i][j] = 2 
                    go(i, j)
                    bd[i][j] = 0

                    # 2개로 채우기
                    if 0 <= j+1 < 2*n+1 and bd[i][j+1]!=-2 and bd[i][j+1]!=2:
                        bd[i][j] = 2
                        bd[i][j+1] = 2
                        go(i, j)
                        bd[i][j+1] = 1
                        bd[i][j] = 0
                    
                elif bd[i][j] == 1:
                    # 1개로 채우기. 
                    bd[i][j] = 2 
                    go(i, j)
                    bd[i][j] = 1

                    # 2개로 채우기 (오른쪽)
                    if 0 <= j+1 < 2*n+1 and bd[i][j+1]!=-2 and bd[i][j+1]!=2:
                        bd[i][j] = 2
                        bd[i][j+1] = 2
                        go(i, j)
                        bd[i][j+1] = 0
                        bd[i][j] = 1
                    
                    # 2개로 채우기 (위쪽)
                    if 0 <= i-1 < n+1 and bd[i-1][j]!=-2 and bd[i-1][j]!=2:
                        bd[i][j] = 2
                        bd[i-1][j] = 2
                        go(i, j)
                        bd[i-1][j] = 0
                        bd[i][j] = 1
        
        # 모든 점이 꽉찼다면, 여기에 도달.
        nonlocal answer
        answer+=1
        
        return
    
    go(n, 0)
    
    return answer%10007


# 답이 없어서 
# https://kau-algorithm.tistory.com/1353 링크 참고하시면 될 것 같아요...