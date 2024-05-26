#https://y-seo.tistory.com/m/entry/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-6236%EB%B2%88-%EC%9A%A9%EB%8F%88-%EA%B4%80%EB%A6%AC
n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start, end = max(arr), sum(arr)
while start <= end:
    mid = (start+end)//2
    curr = mid
    count = 1
    for i in arr:
        if curr - i < 0:
            count+=1
            curr = mid
        curr -= i
    if count > m:
        start = mid+1
    else:
        end = mid-1
        
print(mid)
