'''
팀 조직,

각 원 : 각각의 직원 1명

원 속 2개 숫자
왼쪽 : 직원번호 / 1번 부터 순서대로 발급되는 일련번호
오른쪽 : 해당 직원 하루 평균 매출액

모든 직원은 팀장 or 팀퉌

팀장 팀원 관계 화살표
화살표 가리키는 쪽이 팀원

직원 번호 1 : 회사 CEO, 항상 팀장, 팀원일 수 없음

CEO 제외한 팀원은 다른 누군가로부터 정확히 1개 화살표

한 직원은 최대 2개 팀에 소속될 수 있음
만일 누군가가 2개에 팀에 속해있다면
한 팀의 팀원이면서 다른 팀의 팀장이라는 뜻


워크숍 참석 직원 선발

1. 모든 팀은 최소 1명 이상의 직원을 워크숍에 참석

2. 워크숍에 참석하는 직원의 하루 평균 매출액이 최소가 되야 함

공통으로 속한 직원이면 1명만 참가해도 2팀 모두 참석한것으로 인정




'''
from collections import defaultdict


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]

links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

result = 44

def solution(sales, links):
    answer = 0

    # 팀 트리 딕셔너리
    team = defaultdict(list)
    for up, down in links:
        team[up].append(down)

    # dp 생성, 0은 워크숍 참가 인원, 1은 워크숍 참가 x
    dp = [[0,0]] + [[0, sale]for sale in (sales)]


   


    def dfs(start):
        if not team[start]:
            return
        




    print(team)
    return answer


solution(sales, links)