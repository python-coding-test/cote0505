def solution(lottos, win_nums):
    answer = []
    
    same = 0 # 일치하는 로또 번호 수
    zero = 0 # 알아볼 수 없는 로또 번호 수
    
    for lotto_number in lottos:
        if (lotto_number == 0):
            zero += 1
            continue
        for win_number in win_nums:
            if (lotto_number == win_number):
                same += 1
                break
    
    max_count = same + zero # 최대로 맞추는 수 
    min_count = same # 최소로 맞추는 수
    
    def get_result(n : int, result : []):
        if (n == 6):
            result.append(1)
        elif (n == 5):
            result.append(2)
        elif (n == 4):
            result.append(3)
        elif (n == 3):
            result.append(4)
        elif (n == 2):
            result.append(5)
        else:
            result.append(6)
    
    get_result(max_count, answer)
    get_result(min_count, answer)
    

    return answer