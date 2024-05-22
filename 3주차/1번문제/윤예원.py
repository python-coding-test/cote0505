#블로그 참고https://hillier.tistory.com/106
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
used = [False]*(n+1)
arr = [0]*(2*n+1)
used[y-x-1] = True
arr[x], arr[y] = y-x-1,y-x-1
answer = 0

def dfs(x):
    global answer
    if x == 2*n+1:
        answer+=1
        return
    if arr[x] !=0:
        dfs(x+1)
    else:
        for j in range(1, len(used)):
            if not used[j] and x+j+1 < 2*n+1 and arr[x+j+1] == 0:
                used[j] = True
                arr[x]=j
                arr[x+j+1] = j
                dfs(x+1)
                used[j] = False
                arr[x] = 0
                arr[x+j+1] = 0


dfs(1)