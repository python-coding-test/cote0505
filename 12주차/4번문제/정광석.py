'''
주택 건축

n n 정사각 격자 가상 벽면

기둥은 바닥위에 있거나 보의 한쪽 끝 부분 위에 있거나 다른 기둥 위에 있어야 한다

보는 한쪽 끝 부분이 기둥위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결 되어야 한다





'''	
n = 5

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
#build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


# x,y,a,b = 가로, 세로, a = 0(기둥), 1(보), b = 0(삭제), 1(설치)



'''
각 설치/삭제 할 때마다 가능한지 불가능한지 체크해야 할듯

기둥 설치가 가능하다 = 바닥위(y=0) or 보 한쪽 끝 위(보 왼쪽좌표 and 오른쪽 좌표)  or 다른 기둥 위
보 설치가 가능하다 = 보 한쪽 끝이 기둥위 or 양쪽 끝이 다른 보와 동시에 연결


'''



def solution(n, build_frame):
    answer = []


    def can_install_bo(x,y):
        # 한쪽 끝 부분이 기둥 위에 있음
        if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
            return True

        elif [x-1,y,1] in answer and [x+1,y,1] in answer:
            return True

        return False
    


    

    def can_install_gi(x,y):
    
        if y==0:
            return True
        
        elif [x-1,y,1] in answer or [x,y,1] in answer:
            return True
        
        elif [x,y-1,0] in answer:
            return True
        
        return False
        

    
    def can_remove(x, y, a):
        # 구조물 삭제 시, 다른 모든 구조물이 유효한지 확인
        answer.remove([x, y, a])
        for tx, ty, ta in answer:
            if ta == 0 and not can_install_gi(tx, ty):  # 기둥
                answer.append([x, y, a])
                return False
            if ta == 1 and not can_install_bo(tx, ty):  # 보
                answer.append([x, y, a])
                return False
        return True
        
        
        
        
    




    for order in build_frame:
        x,y,a,b = order
        if b == 1: # 설치하기
            if a==0 : #기둥 설치
                if can_install_gi(x,y):
                    answer.append([x,y,a])
            elif a==1 : #보 설치
                if can_install_bo(x,y):
                    answer.append([x,y,a])

            #print(answer)
        elif b == 0 : # 삭제하기
            
            can_remove(x,y,a)
                
                





    answer.sort()
    return answer


print(solution(n,build_frame))