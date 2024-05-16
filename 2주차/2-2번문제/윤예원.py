import math, sys
input = sys.stdin.readline
a,b = map(int, input().split())
arr = [False]+[False]+[True for _ in range(2,b+1)]


for i in range(2, int(math.sqrt(b))+1):
    if arr[i] == True:
        j = 2
        while i*j <= b:
            arr[i*j] = False
            j+=1


count = sum(arr[a:b+1])

print(count)




