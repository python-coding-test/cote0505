import sys
N, S = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

l = 0
r = 0
length = 100000
tmp_sum = ls[0]

while l <= r:
    if tmp_sum >= S:
        length = min(length, r - l + 1)
        tmp_sum -= ls[l]
        l+=1
    else:
        r+=1
        if r < N:
            tmp_sum += ls[r]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)