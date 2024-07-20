from collections import defaultdict

def plusTime(e,s):
    eh,em = map(int,e.split(':'))
    sh,sm = map(int,s.split(':'))

    if em < sm:
        eh -= 1
        em += 60
    return (eh-sh)*60 + (em-sm)

def solution(fees, records):
    in_log = {}
    fee_log = defaultdict(int)
    for record in records:
        time, carNum, inOut = record.split(' ')
        if inOut == 'IN':
            in_log[carNum] = time
        else:
            fee_log[carNum] += plusTime(time,in_log[carNum])
            del in_log[carNum]

    for i,v in in_log.items():
        fee_log[i] += plusTime("23:59",v)

    fee_log = dict(sorted(fee_log.items()))
    res = []
    for time in fee_log.values():
        fee = fees[1]
        if time > fees[0]:
            overTime = (time-fees[0])//fees[2]
            if (time-fees[0])%fees[2]:
                overTime += 1
            fee += overTime*fees[3]
        res.append(fee)

    return res