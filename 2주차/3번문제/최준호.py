import sys

while 1:
    n = int(sys.stdin.readline())
    if n==0:
        break

    incomes = [int(sys.stdin.readline()) for _ in range(n)]
    curMax = incomes[0]
    globalMax = incomes[0]

    for i in range(1, n):
        curMax = max(incomes[i], incomes[i]+curMax)
        globalMax = max(globalMax, curMax)
    print(globalMax)