# 통과 못한 풀이입니다. 반례를 못 찾겠어요ㅠ
N, M = map(int, input().split())
K = int(input())
city = [[0]*(M+1) for _ in range(N+1)]

blocking = set()
block_x, block_y = -1,-1
for _ in range(K):
    a,b,c,d = map(int, input().split())
    if a==c:
        if a == 0:
            block_y = max(b,d)
        elif b>d:
            blocking.add((c,d,a,b))
        else:
            blocking.add((a,b,c,d))
    elif b==d:
        if b==0:
            block_x = max(a,c)
        if a>c:
            blocking.add((c,d,a,b))
        else:
            blocking.add((a,b,c,d))

for i in range(1,N+1):
    if i == block_x:
        break
    city[i][0] = 1
for i in range(1,M+1):
    if i == block_y:
        break
    city[0][i] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        prev_a = city[i-1][j] if (i-1,j,i,j) not in blocking else 0
        prev_b = city[i][j-1] if (i,j-1,i,j) not in blocking else 0
        city[i][j] = prev_a + prev_b

print(city[-1][-1])