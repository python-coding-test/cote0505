import math

def solution(fees, records):
    
    base_time, base_fee, unit_time, unit_fee = map(int, fees)
    
    
    ### 1. 차량 주차 시간 구하기.

    parking_times = {}
    # 차량 번호 : 누적시간
    
    parking_check = {}
    # 차량 번호 : 입차 시간 기록.
    
    parking_fee = {}
    # 차량 번호 : 요금 기록
    
    parking_car_nums = []
    # 차량 번호
    
    
    
    for re in records:
        in_time, car_num, in_and_out = re.split()
        
        hour, minute = map(int, in_time.split(':'))
        total_time = hour*60 + minute
                
        if in_and_out == 'IN': # 만약 입차인 경우.
            parking_check[car_num] = total_time
            
        else : # 만약 출차인 경우.
            if car_num not in parking_times: # 이미 한번 주차장 방문 기록 있다면.
                parking_times[car_num] = (total_time - parking_check[car_num])
            else :
                parking_times[car_num] += (total_time - parking_check[car_num])
            
            del parking_check[car_num]
    
    if parking_check: # 만약 출차 기록이 남아있지 않은게 존재한다면.
        for car_num, in_time in parking_check.items():
            
            out_time = 23*60 + 59 # 23:59에 출차한 것으로 간주.
            
            if car_num not in parking_times: # 이미 한번 주차장 방문 기록 있다면.
                parking_times[car_num] = (out_time - in_time)
            else :
                parking_times[car_num] += (out_time - in_time)
    
    ### 2. 차량 번호별 요금 구하기.
    
    for car_num, total_time in parking_times.items():
        parking_car_nums.append(car_num)
        
        if total_time <= base_time:
            parking_fee[car_num] = base_fee
        else:
            parking_fee[car_num] = base_fee + math.ceil((total_time-base_time) / unit_time)*unit_fee
    
    ### 3. 결과 출력.
    
    # 차량 번호 오름차순 정렬
    parking_car_nums.sort()
    
    # 각 차량 번호 별 요금 출력.
    answer = [parking_fee[car_num] for car_num in parking_car_nums]
    
    return answer