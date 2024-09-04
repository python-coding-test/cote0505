'''
베로니

카드 짝 맞추기

화면에 카드 16장 뒷면을 위로 4*4 격자 형태

앞 캐릭터

8개 캐릭터가 2장씩 무작위

두장 선택했을 때 같은 그림이면 사라짐
같은 그림이 아니면 뒷면이 보이도록 다시 뒤집힘

모든 카드 화면에서 사라지게 하면 게임 종료

커서로 선택

커서 : 4*4 화면에서 유저가 선택한 현재 위치 표시

컨트롤 키, 방향키
상하좌우 : 1칸 이동
컨트롤 + 상하좌우 : 그 방향의 가장 가까운 카드로 한번에// 없으면 끝으로

커서가 카드 뒤집으려면 엔터키

이동 횟수 1
엔터 클릭 횟수 1


모든 카드를 제어하기 위한 키 조작 횟수 최솟값 리턴

r,c에서 시작하는 거
'''

from collections import defaultdict

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]	
r = 1
c = 0

def ctrl_move():
    pass


def solution(board, r, c):
    answer = 0
    
    card = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card[board[i][j]].append([i,j])

    card = dict(card)
    print(card)                

    return answer



solution(board, r,c)