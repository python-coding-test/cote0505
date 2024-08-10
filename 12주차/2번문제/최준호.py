# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%9B%84%EB%B3%B4%ED%82%A4-Python
# 위 블로그 참고했습니다!

from itertools import combinations

def solution(relation):
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합
    idx = []
    for i in range(1, col+1):
        idx.extend(combinations(range(col), i))

    #유일성
    candidate = []
    for i in idx:
        tmp = []
        for row in relation:
            rowTuple = tuple(row[key] for key in i)
            tmp.append(rowTuple)

        if len(set(tmp)) == len(relation):    # 유일성
            put = True

            for x in candidate:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put: candidate.append(i)
    return len(candidate)