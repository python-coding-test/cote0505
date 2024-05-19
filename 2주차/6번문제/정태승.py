import sys

N = int(sys.stdin.readline())

n_idx = 0
n = 0
while True:
    if n_idx > 1000000:
        print(-1)
        exit()
    s = str(n) 
    prev, chk = 0, True
    for i in range(1, len(s)):
        if s[prev] <= s[i]:
            chk = False
            break
        prev = i
    if chk :
        n_idx+=1
        if n_idx == N:
            print(n)
            exit()
    n+=1

# 시간초과