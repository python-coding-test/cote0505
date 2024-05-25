import sys, math

N, M = map(int, sys.stdin.readline().split())

spends=[]
for i in range(N):
    spends.append(int(sys.stdin.readline()))



def go(k):
    withdraw_cnt = 0
    money = 0
    for s in spends:
        if money < s:
            money = k
            withdraw_cnt += 1 # 인출은 딱 한번만.
            # money = math.ceil(s/k) * k # 잔액 입금하고 s원보다 커질때까지 더하기
            # withdraw_cnt+= math.ceil(s/k) # 이건 여러번 인출 가능할때 쓰는 값임.

        money = money - s
        if money < 0:
            return N+1 # max값.
    return withdraw_cnt 


hi = sum(spends)
lo = 1
ans = hi

while lo <= hi:
    
    mid = (lo+hi)//2

    t = go(mid)

    if t > M : # M번 넘을 때.
        lo = mid+1
    else: # M번 이하 일떄.
        hi = mid-1
        ans = min(ans, mid)
  
print(ans)  