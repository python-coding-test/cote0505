#블로그https://woongtech.tistory.com/entry/C-python-BOJ-%EB%B0%B1%EC%A4%80-1577-%EB%8F%84%EB%A1%9C%EC%9D%98-%EA%B0%9C%EC%88%98
n,m = map(int, input().split()) #가로, 세로
k = int(input())
road = []
for _ in range(k):
    road.append(list(map(int, input().split())))
dp = [[0]*(n+1) for _ in range(m+1)]
dp[0][0] = 1

def check(cur, a,b,c,d):
    return cur == [a,b,c,d] or cur == [c,d,a,b]
    


for y in range(m+1):
    for x in range(n+1):
        if y > 0:
            for a,b,c,d in road:
                if check([x, y-1, x, y], a,b,c,d):
                    break
            else:
                dp[y][x] += dp[y-1][x]
        if x>0:
            for a,b,c,d in road:
                if check([x-1,y,x,y],a,b,c,d):
                    break
            else:
                dp[y][x] += dp[y][x-1]

print(dp[m][n])