import math

def ceil(x):
    return math.ceil(x)

def solution(fees, records):
    answer = []
    records_dict = {}
    sorted_records_dict = {}
    
    # 입력 값을 딕셔너리에 저장.
    for record in records:
        record_arr = record.split(' ')
        car_number = int(record_arr[1])
        if car_number not in records_dict:
            records_dict[car_number] = []
        records_dict[car_number].append([record_arr[0], record_arr[2]])
    
    # print(records_dict)
    # {5961: [['05:34', 'IN'], ['07:59', 'OUT'], ['22:59', 'IN'], ['23:00', 'OUT']], 
    #  0: [['06:00', 'IN'], ['06:34', 'OUT'], ['18:59', 'IN']], 148: [['07:59', 'IN'], ['19:09', 'OUT']]}
    
    # 차량 번호 순으로 정렬.
    for car_number in sorted(records_dict.keys()):
        sorted_records_dict[car_number] = records_dict[car_number]
        
    #print(sorted_records_dict)
    # {0: [['06:00', 'IN'], ['06:34', 'OUT'], ['18:59', 'IN']], 
    # 148: [['07:59', 'IN'], ['19:09', 'OUT']], 5961: [['05:34', 'IN'], ['07:59', 'OUT'], ['22:59', 'IN'], ['23:00', 'OUT']]} 
    
    for car_number, records in sorted_records_dict.items():
        in_flag = False
        in_hour = 0
        in_minute = 0
        total_time = 0
        for record in records:
            hour, minute = map(int, record[0].split(':'))
            if (record[1] == 'IN'):
                in_hour = hour
                in_minute = minute
                in_flag=True
            else:
                diff_hour = hour-in_hour
                diff_minute = minute-in_minute
                total_time += diff_hour*60 + diff_minute
                in_hour = 0
                in_minute = 0
                in_flag=False
        if (in_flag):
            diff_hour = 23-in_hour
            diff_minute = 59-in_minute
            total_time += diff_hour*60 + diff_minute
            
        #print(f"total_time : {total_time}")
        
        if (total_time > fees[0]):
            total_money = fees[1] + ceil((total_time - fees[0])/fees[2])*fees[3]
        else:
            total_money = fees[1]
        #print(f"total_mony : {total_money}")
        
        answer.append(total_money)
        
    return answer