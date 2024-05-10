from collections import deque
n = int(input())
arr = list(map(int, input().split()))
s = int(input())
visited = [False]*n
cur_loc = 0
def bfs(m):

    queue = deque()
    queue.append(m)
    visited[m] = True
    while queue:
        x = queue.popleft()
        cur_loc = x+ arr[x]
        if 0<=cur_loc<n and not visited[cur_loc]:
            queue.append(cur_loc)
            visited[cur_loc] = True

        cur_loc1 = x- arr[x]
        if 0<=cur_loc1<n and not visited[cur_loc1]:
            queue.append(cur_loc1)
            visited[cur_loc1] = True
bfs(s-1)   
true_count = visited.count(True)    
print(true_count)