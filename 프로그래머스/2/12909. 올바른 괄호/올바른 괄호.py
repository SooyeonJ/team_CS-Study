def solution(s):
    answer = True
    lcnt = 0
    rcnt = 0
    for i, val in enumerate(s):
        if val == '(':
            lcnt += 1
        else:
            rcnt += 1
        if lcnt < rcnt:
            answer = False
    if lcnt != rcnt:
        answer = False    
    return answer