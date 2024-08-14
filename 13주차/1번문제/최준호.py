from collections import defaultdict, deque

oil = {}

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def calculateOil(land, q):
    cnt = 0

    while q:
        x,y,num = q.popleft()

        if land[x][y] == num:
            continue

        land[x][y] = num
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]:
                q.append((nx,ny,num))
    return cnt

def solution(land):
    q = deque()
    for i in range(len(land[0])):
        for j in range(len(land)):
            if land[j][i]:
                q.append((j,i))

    num = 1
    while q:
        x,y = q.popleft()
        num += 1
        if land[x][y] > 1:
            continue
        cnt = calculateOil(land,deque([(x,y,num)]))
        if not cnt:
            continue
        oil[num] = cnt

    maxCnt = 0
    for i in range(len(land[0])):
        rowCntSet = set()
        rowCnt = 0
        for j in range(len(land)):
            if land[j][i]:
                rowCntSet.add(land[j][i])
        for rc in rowCntSet:
            rowCnt += oil[rc]
        maxCnt = max(maxCnt, rowCnt)

    return maxCnt