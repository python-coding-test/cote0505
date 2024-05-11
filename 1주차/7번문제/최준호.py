from bisect import bisect_left

k = int(input())

rule = []
temp = 2
while temp < k:
    rule.append(temp)
    temp *= 2

cnt = 0
while k > 2:
    idx = bisect_left(rule, k)
    if idx == len(rule) or rule[idx] >= k:
        idx -= 1
    k -= rule[idx]
    cnt += 1

ans = ['0','1']
if cnt % 2:
    print(ans[2-k])
else:
    print(ans[k-1])