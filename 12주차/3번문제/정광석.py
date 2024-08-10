'''

자물쇠와 열쇠

n n 크기 정사각 격자

열쇠는 m m 정사각 격자

홈, 돌기

열쇠는 회전과 이동 가능


열쇠의 돌기 부분을 자물쇠의 홈 부분에 맞게 채우자




'''
# 실패

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	

lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

result = True

def rotate(array_2d):
    # 시계방향 90도
    n = len(array_2d)
    result = [[0] * n for _ in range(n)] 

    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = array_2d[i][j]
    return result



def check(x,y,m):

    for i in range(m):
        for j in range(m):
            if 0<=x+i<m and 0<=y+j<m:
                if lock[x+i][y+j] + key[i][j] != 1:
                    return False
                
    return True



def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)
    for _ in range(4):
        key = rotate(key)
        for x in range(-m+1, n):
            for y in range(-m+1, n):
                if check(x,y,m):
                    return True
    return False
    

# 3중 for?

print(solution(key, lock))
