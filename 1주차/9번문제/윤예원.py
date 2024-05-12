import sys
input = sys.stdin.readline
n,t,p = map(int, input().split())
time = [[0]*2 for _ in range(t)]
for i in range(t):
    s,e = map(int, input().split())
    time[i][0] =int(s[:1])*60 + s[2:]
    time[i][1] =int(e[:1])*60 + e[2:]
time.sort(key = lambda x :(x[0], x[1]))
start = time[0][0]
end = time[0][1]

def compare(visited, count, time):
    


    distances = [abs(p -1), abs(p - n)]

    # Find the maximum distance
    max_distance = max(distances)
    if distances[0] == distances[1]:
        return 1
    elif distances[0] == max_distance:
        return 1
    else:
        return p
    
sit = [0]*t
sit[1] = end
visited = [False]*(n+1)
visited[1] = end
cur = 1
count = 0

for i in range(1, t):
    if end <time[i][0]:
        a= compare(visited, count,time[i][0])
        if sit[a] < time[i][0]:
            sit[p] = end
        else:




