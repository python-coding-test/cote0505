import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))


interval_sum = 0
start, end  = 0, 0
min_length = sys.maxsize
while True:
    if interval_sum >= s:
        min_length = min(min_length, end-start)
        interval_sum -= arr[start]
        start+=1
    elif end == n:
        break
    else:
        interval_sum+=arr[end]
        end+=1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
    