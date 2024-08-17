# 요걱 시스템

'''

참고: https://velog.io/@mang0206/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9A%94%EA%B2%A9-%EC%8B%9C%EC%8A%A4%ED%85%9C-python

'''

import sys

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]


def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    # print(targets)
    end = 0
    for i in targets:
        if i[0] >= end:
            answer += 1
            end = i[1]
    return answer


print(solution(targets))
