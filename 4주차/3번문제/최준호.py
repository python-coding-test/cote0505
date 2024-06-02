from itertools import combinations
from bisect import bisect_left

def simulate(dice, choice, cur, tempSum, sumRes):
    if cur == len(choice):
        sumRes.append(tempSum)
        return
    for num in dice[choice[cur]]:
        simulate(dice, choice, cur+1, tempSum+num, sumRes)

def solution(dice):
    answer = []

    # 주사위 조합 구하기
    choices = []
    for i in range(len(dice)):
        choices.append(i)

    half = len(dice) // 2
    A_choices = list(combinations(choices, half))

    # 각 주사위 조합 별 합 구하기
    sum_res = {}
    for i,v in enumerate(A_choices):
        temp = []
        simulate(dice, v, 0, 0, temp)
        temp.sort()
        sum_res[i] = temp

    # A가 선택한 조합별 합과 B가 선택한 조합별 합을 비교해서 best 찾아내기
    best = 0
    for k,v in sum_res.items():
        A = v
        B = sum_res[len(A_choices)-k-1]

        cnt = 0
        for i in A:
            cnt += bisect_left(B,i)

        if cnt > best:
            best = cnt
            answer = sorted(A_choices[k])

    for i in range(len(answer)):
        answer[i] += 1

    return answer