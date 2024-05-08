import sys

N, K = map(int, sys.stdin.readline().split())

cargos = {}
dp = {}

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    cargos[i] = (W, V)

def go(k, level):
    if level == N: # 짐 최대 개수 도달
        return 0
    
    if (k, level) in dp:
        return dp[(k, level)]
    
    dp[(k, level)] = -1
    if k >= cargos[level][0]: # 현재 배낭 남은 무게가 충분할때
        dp[(k, level)] = max(go(k-cargos[level][0], level+1)+cargos[level][1], dp[(k, level)]) # 넣기
    
    dp[(k, level)] = max(go(k, level+1), dp[(k, level)]) # 안 넣기

    return dp[(k, level)]


print(go(K, 0))