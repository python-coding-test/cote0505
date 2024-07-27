from math import ceil # 올림


def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    
    car_in = {}  # 입차 기록 -> 번호: 입차 시간
    using_time = {}  # 누적 사용 시간 기록 -> 번호: 누적 시간
    
    for i in records:
        time, number, io = i.split()
        hour, minute = map(int, time.split(":"))
        temp_time = hour * 60 + minute
        
        if io == "IN":
            car_in[number] = temp_time  # 입차 시간 기록
            
        else:
            # 차량번호가 using_time 딕셔너리에 존재
            if number in using_time:
                using_time[number] += (temp_time - car_in[number])  # 누적
            else:
                using_time[number] = (temp_time - car_in[number])  # 할당
            del car_in[number]  # 출차 후 입차 기록 제거
        
    # 하루 종료 시각까지 출차되지 않은 차량 처리
    for number, time in car_in.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time
    
    # 차량번호 순으로 요금 계산
    for number, time in sorted(using_time.items(), key = lambda x: x[0]):
        fee = default_fee + max(0, ceil((time-default_time)/unit_time)) * unit_fee
        answer.append(fee)
        
    return answer
