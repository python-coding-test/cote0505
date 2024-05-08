import sys
from collections import deque

N = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

def bfs(st):
    q = deque()
    q.append(st)
    vis = {st:True}
    res = 1
    while q:
        if res == len(stones):
            return res
        curr = q.popleft()
        # for d in range(1, stones[curr]+1): # 1부터 최대 stones[st]까지 움직을 수 있음.
        for nxt in [curr-stones[curr], curr+stones[curr]]: # 왼쪽 혹은 오른쪽
            # if nxt >= len(stones) :
            #     nxt = len(stones)-1
            # elif nxt < 0 :
            #     nxt = 0

            if 0 <= nxt < len(stones) and nxt not in vis:
                q.append(nxt)
                vis[nxt] = True
                res+=1
    
    return res

print(bfs(s-1)) # s는 1부터N이니깐 s-1로 표시.

# 방문한 곳 또 방문 가능?
# 문제 자체가 이해가 어려웠음.. 아래링크 참고해서 품
# https://yeoooo.github.io/algorithm/BOJ14248/