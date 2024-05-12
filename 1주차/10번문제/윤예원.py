import sys
s = list(input())
t = list(input())
def dfs(t):
    if t == s:
        print(1)
        sys.exit()
    if len(t) == 0:
        return 0
    if t[-1] == "A":
        dfs(t[:-1])
    if t[0] == "B":
        dfs(t[1:][::-1])
    
dfs(t)
print(0)

