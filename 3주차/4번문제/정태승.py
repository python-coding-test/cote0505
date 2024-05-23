import sys
sys.setrecursionlimit(10**5)

T = int(sys.stdin.readline())
dp = {}
def go(n, prev):

    if n == 0:
        return 1
    
    if n < 0 :
        return 0
    
    if (n, prev) in dp:
        return dp[(n, prev)]
    n1 = go(n-1, 1) if prev!=1 else 0 
    n2 = go(n-2, 2) if prev!=2 else 0 
    n3 = go(n-3, 3) if prev!=3 else 0 
    dp[(n, prev)] =  n1 + n2 + n3

    return dp[(n, prev)]%1000000009


for _ in range(T):
    n = int(sys.stdin.readline())   

    print(go(n, -1)%1000000009)


