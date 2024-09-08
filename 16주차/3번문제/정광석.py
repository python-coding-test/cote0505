'''
0~N-1 번호 매겨있는 N개의 도시, 두 도시 연결하는 도로

A, B 가 x로 C, D가 y로 연결되어 있으면
() 가 큰 쪽의 도로 우선순위가 크다.

우선순위에 대한 내림차순으로 정렬
집합 사이에도 우선순위가 있음

한 집합에 있는 도로만으로 임의의 도시에서 임의의 도시로 이동할 수 있을 때
집합이 연결되어 있다.


출력 : 
정답이 없으면 -1
존재하면 집합에 속하는 도로 중 0을 끝점으로 갖는 개수
1을 끝점으로 갖는 개수
..
N-1을 끝점으로 갖는 도로의 개수를 차례로 출력한다

'''


def find_parent(parent, a):
    if a == parent[a]: return a
    return find_parent(parent, parent[a])

def union(parent ,a, b):
    na = find_parent(parent, a)
    nb = find_parent(parent, b)
    if na<nb:
        parent[nb] = na
    else:
        parent[na] = nb

#입력
n, m = map(int, input().split())
board=[]
answer = []
temp = []
parent = [i for i in range(n)]
cntlist = [0 for _ in range(n)]

for _ in range(n):
    board.append(list(input().strip()))



y_cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if board[i][j]=='Y':
            #print("parent",find_parent(parent, i), find_parent(parent, j))
            if find_parent(parent,i) == find_parent(parent,j):
                # 부모가 같으면 우선순위가 낮음
                temp.append((i,j))
                y_cnt+=1
            else:
                y_cnt +=1
                answer.append((i,j))
                union(parent, i,j)


root = find_parent(parent, 0)
#print(y_cnt)
for i in range(1, n):
    if find_parent(parent, i) != root or y_cnt < m:
        print(-1)
        exit()

answer += temp
for i in range(m):
    s,e = answer[i]
    cntlist[s]+=1
    cntlist[e]+=1

# print(cntlist)
# print("answer",answer)
# print("parent", parent)



for i in cntlist:
    print(i, end=' ')