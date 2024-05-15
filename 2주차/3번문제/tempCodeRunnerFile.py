import sys

while 1:
    n = int(sys.stdin.readline())
    if n==0:
        break

    incomes = []
    minMinus = -10000
    for _ in range(n):
        income = int(sys.stdin.readline())
        if not incomes and income < 0:
            minMinus = max(minMinus, income)
            continue

        if income >= 0:
            if len(incomes)%2:
                incomes[-1] += income
            else:
                incomes.append(income)
        else:
            if not len(incomes)%2:
                incomes[-1] += income
            else:
                incomes.append(income)

    if not incomes:
        print(minMinus)
        continue

    maxIncome = incomes[0]
    temp = 0
    for i in range(2,len(incomes),2):
        if incomes[i] + incomes[i-1] >= 0:
            maxIncome += (incomes[i] + incomes[i-1])
        else:
            temp = max(temp, maxIncome)
            maxIncome = incomes[i]
    temp = max(temp, maxIncome)
    print(temp)