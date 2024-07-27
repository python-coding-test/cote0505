'''

< 로직 >

알고리즘: 해시테이블(딕셔너리), 이진탐색

1. make_case 함수
주어진 지원자 정보를 다양한 조합의 키로 변환하여 infoDict에 저장 (조건 검색을 쉽게 하기 위해)

2. find_answer 함수
이진 탐색을 사용하여 쿼리 점수보다 큰 점수들의 개수를 빠르게 찾음
bisect_left를 사용하여 해당 점수 이상의 첫 번째 위치를 찾고, 그 위치부터 끝까지의 개수를 반환

3. solution 함수
info 리스트를 순회하며 각 지원자 정보를 다양한 조합의 키로 변환하여 infoDict에 저장
각 키에 대한 점수 리스트를 오름차순으로 정렬 (이진 탐색을 사용할 수 있도록 준비)
query 리스트를 순회하며 각 쿼리를 파싱하고, 해당 조건에 맞는 지원자 수를 찾아 결과 리스트에 추가

'''

from itertools import combinations
from bisect import bisect_left

# 주어진 지원자의 정보를 다양한 조합의 키로 변환하여 infoDict에 저장하는 함수
def make_case(x, infoDict):
    tempArr = x.split(" ")  # 지원자의 정보를 공백으로 분리
    score = int(tempArr[-1])  # 마지막 요소는 점수이므로 이를 정수로 변환
    for idx in range(5):  # 0부터 4까지의 인덱스에 대해
        for c in combinations(tempArr[:-1], idx):  # 점수를 제외한 나머지 정보의 모든 조합 생성
            key = "".join(c)  # 조합된 정보를 하나의 문자열로 결합하여 키로 사용
            if key in infoDict:  # 키가 이미 infoDict에 있는 경우
                infoDict[key].append(score)  # 해당 키에 점수를 추가
            else:
                infoDict[key] = [score]  # 키가 없는 경우 새로운 리스트로 초기화하고 점수를 추가

# 이진 탐색을 통해 쿼리 점수보다 큰 점수들의 개수를 반환하는 함수
def find_answer(key, queryScore, infoDict):
    if key in infoDict:  # 주어진 키가 infoDict에 있는 경우
        # 이진 탐색을 통해 queryScore보다 큰 점수들의 개수 계산
        return len(infoDict[key]) - bisect_left(infoDict[key], queryScore)
    return 0  # 키가 없는 경우 0을 반환

def solution(info, query):
    infoDict = dict()  # 정보 저장을 위한 딕셔너리 초기화
    
    for x in info:
        make_case(x, infoDict)  # 각 지원자 정보를 다양한 조합의 키로 변환하여 infoDict에 저장
    
    for key in infoDict.keys():
        infoDict[key].sort()  # 각 키에 대한 점수 리스트를 오름차순으로 정렬
        
    answer = []
    for x in query:
        # "and"를 공백으로 대체하고, "-"는 제거한 후 각 요소를 분리하여 리스트로 저장
        tempArr = list(y for y in x.replace("and", " ").replace("-", "").split(" ") if len(y) > 0)
        queryScore = int(tempArr[-1])  # 마지막 요소는 쿼리 점수이므로 이를 정수로 변환
        if len(tempArr) == 1:  # 조건이 모두 "-"인 경우
            answer.append(find_answer("", queryScore, infoDict))
        else:
            answer.append(find_answer("".join(tempArr[:-1]), queryScore, infoDict))  # 조건을 키로 변환하여 점수 검색
            
    return answer  # 최종 결과 반환



'''
기존 방법 -> 정확성은 다 맞는데, 효율성에서 시간초과로 틀림
'''
# def solution(info, query):
#     answer = []
#     target = {}
        
#         for j in info:
#             a, b, c, d, e = j.split()
#             e = int(e)
#             if ((a == langue) or (langue == '-')) and ((b == pos) or (pos == '-')) and ((c == step) or (step == '-')) and ((d == food) or (food == '-')) and ((e >= score) or (score == '-')):
#                 count += 1
#         answer.append(count)
        
#     return answer
