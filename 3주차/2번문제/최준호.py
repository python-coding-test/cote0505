N,S = map(int, input().split())
arr = list(map(int, input().split()))

l,r = 0,0
temp = arr[l]
minLength = len(arr) + 1
while l <= r:
    if temp < S:
        r += 1
        if r == N:
            break
        temp += arr[r]
    else:
        minLength = min(minLength, r-l+1)
        temp -= arr[l]
        l += 1

if minLength == len(arr) + 1:
    print(0)
else:
    print(minLength)