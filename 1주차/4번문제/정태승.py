import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))

res = 0
def combi(st, curr):
    if len(curr) == 3:
        curr = list(map(lambda x : points[x], curr)) # 점 대응시켜주기.
        a = (curr[0][0]-curr[1][0])**2 + (curr[0][1]-curr[1][1])**2
        b = (curr[0][0]-curr[2][0])**2 + (curr[0][1]-curr[2][1])**2
        c = (curr[1][0]-curr[2][0])**2 + (curr[1][1]-curr[2][1])**2# 길이
        lens = [a,b,c] # 정렬
        lens.sort()
        if lens[2] == lens[0] + lens[1]: # 피타고라스
            global res
            res += 1
        return
    
    for i in range(st+1, N):
        if i in curr:
            continue

        curr.append(i)
        combi(i, curr)
        curr.pop()
    
    return

combi(-1, [])
print(res)

# 1. 점 3개 고르기
# 2. 점 3개로 a^2 = b^2+c^2 구하기
# N**3 풀이. 시간초과발생.
# 이 문제는 너무 수학적인 문제라 넘어갈게요..
# https://lighter.tistory.com/37