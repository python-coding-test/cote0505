from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dict = defaultdict(list)
    
    for info in information:
        info_list = info.split(" ")
        user_info = info_list[:-1]
        #print(f"user_info : {user_info}")
        score=int(info_list[-1])
        #print(f"score : {score}")
        for i in range(0,5):
            combination_list = list(combinations([0, 1, 2, 3], i))
            # print(f"combination_list : {combination_list}")
            for case in combination_list:
                tmp = user_info.copy()
                for i in case:
                    tmp[i]="-"
                #print(f"tmp : {tmp}")
                dict_key = "".join(tmp)
                dict[dict_key].append(score)
        #for key, value in dict.items():
        #    print(f"key, value : {key}, {value}")
        
    for value in dict.values():
        value.sort()
        
    for q in queries:
        query = q.replace(" and ", " ").split()
        #print(f" query: {query}")
        q_info = ''.join(query[:-1])
        q_score = int(query[-1])
        #print(f"q_info : {q_info}")
        count = 0
        if q_info in dict:
            target_list = dict[q_info]
            idx = bisect_left(target_list, q_score) # Lower Bound는 '원하는 값 이상이 처음 나오는 위치를 찾는 과정'
            count = len(target_list) - idx
        answer.append(count)
    return answer