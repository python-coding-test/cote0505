fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", 
           "06:34 0000 OUT", "07:59 5961 OUT", 
           "07:59 0148 IN", "18:59 0000 IN", 
           "19:09 0148 OUT", "22:59 5961 IN", 
           "23:00 5961 OUT"]

result = [14600, 34400, 5000]



# fees = [기본시간, 기본요금, 단위시간, 단위요금]
# 기본시간  이하라면 기본요금청구, 기본 시간 초과시 초과한시간에 대해서 단위 시간당 단위 요금 청구


# 초과 시간이 단위 시간으로 나눠떨어지지 않으면 올림

# 출차 내역이 없으면 23:59 에 나갔다고 간주


import math

# def solution(fees, records):
#     answer = []
#     dtime, dfee, times, fees = map(int, fees)


#     parkinglot = [] # 주차장에 있는 차 번호 저장
#     total_fee = {} # 차별로 최종 금액 계산
#     parking_time = {} # 차별로 주차 시간 계산
#     total_time = {} # 차별로 총 주차시간 계산
    
    
#     for r in records:
#         time,num,io = r.split()
#         hh,mm = map(int, time.split(':'))
#         conv_time = hh*60 + mm

#         if io == "IN":
#             parking_time[num] = conv_time
#             # in 되면  
        
#         else:
#             # out 일때
#             if num in total_time: # 주차장 차를 댄적이 있을 때
#                 total_time[num] += (conv_time - parking_time[num])
#                 del parking_time[num]
                
#             else:
#                 total_time[num]= (conv_time - parking_time[num])
#                 del parking_time[num]
            
#         for number, time in parking_time.items():
#             if number in parking_time:
#                 total_time[number] += 23*60+59 - time
#             else:
#                 total_time[number] = 23*60+59 - time

#         for num, time in sorted(total_time.items(), key = lambda x:x[0]):
#             answer.append(dfee + max(0,math.ceil((time-dtime)/times))*fees)
        
    
#     return answer

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    parking = {}
    using_time = {}
    for record in records:
        time, number, io = record.split()
        hour, minute = map(int,time.split(":"))
        time = hour * 60 + minute
        if io == "IN":
            parking[number] = time
        elif io == "OUT":
            if number in using_time:
                using_time[number] += (time - parking[number])
            else:
                using_time[number] = time - parking[number]
            del parking[number]
    for number, time in parking.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time
    for number, time in sorted(using_time.items(), key = lambda x:x[0]):
        answer.append(default_fee+ max(0,math.ceil((time-default_time)/unit_time)) * unit_fee)
    return answer

print(solution(fees,records))



