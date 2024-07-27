

lottos = [0, 0, 0, 0, 0, 0]#[45, 4, 35, 20, 3, 9][0, 0, 0, 0, 0, 0]#[44, 1, 0, 0, 31, 25]
win_nums = [38, 19, 20, 40, 15, 25]#[20, 9, 3, 45, 4, 35][38, 19, 20, 40, 15, 25]#[31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    answer = []
    cnt = 0 # 맞춘 번호 개수
    zero_cnt = 0 # 0 개수
    for my_num in lottos:
        
        if my_num==0:
            zero_cnt +=1


        if my_num in win_nums:
            cnt +=1

    
    

    max_cnt = cnt + zero_cnt
    print(max_cnt)
    min_cnt = cnt
    print(min_cnt)

    def rank(x):
        if x<2:
            return 6
        else:
            return 7-x

    hrank = rank(max_cnt)
    lrank = rank(min_cnt)

    
    
    answer = [hrank, lrank]

    return answer



print(solution(lottos, win_nums))
