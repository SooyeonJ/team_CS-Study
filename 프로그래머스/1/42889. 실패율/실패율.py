def solution(N, stages):
    answer = []
    fail = []
    total = len(stages)
    for i in range(1, N+1):
        if total == 0:
            fail.append(0)
        else:
            fail.append(stages.count(i) / total)
            total = total - stages.count(i)    
    answer = sorted(enumerate(fail, 1), key=lambda x:x[1], reverse=True)
    return [x[0] for x in answer]