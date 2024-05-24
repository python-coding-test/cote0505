import sys

n,x,y = map(int, input().split())
used = [0]*(n+1) # 숫자 사용 여부
arr = [0]*(2*n+1)

used[y-x-1] = 1
arr[x] = arr[y] = y-x-1

ans = 0
def dfs(idx):
    global ans

    # 모든 위치 탐색 시, 카운트 증가
    if idx == 2*n+1:
        ans += 1
        return

    # 현재 위치에 값이 할당되어 있을 시, 다음 위치로
    if arr[idx]:
        dfs(idx+1)
        return

    # 사용하지 않은 모든 숫자(i)에 대해서 시도
    for i in range(1, len(used)):
        # 숫자 i를 현재 위치와 현재위치 + i +1 에 배치할 수 있는지 확인
        if not used[i] and idx+i+1 < 2*n+1 and not arr[idx+i+1]:
            # 숫자 i를 각 위치에 배치하고 dfs를 계속
            used[i] = 1
            arr[idx] = i
            arr[idx+i+1] = i

            dfs(idx+1)

            #백트래킹 (이전 상태로 되돌림)
            used[i] = 0
            arr[idx] = 0
            arr[idx+i+1] = 0

dfs(1)
print(ans)





