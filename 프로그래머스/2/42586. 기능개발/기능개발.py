def solution(progresses, speeds):
    days = []
    remainArray = []
    answer = []
    cnt = 1
    for i  in  progresses:
        i = 100 - i
        remainArray.append(i)
    for val, j in enumerate(remainArray):
        if (remainArray[val] % speeds[val]) == 0: 
            days.append(remainArray[val] // speeds[val])
        else: 
            days.append(remainArray[val] // speeds[val] + 1) 
        
    # 배포 기준(base) vs 다음 원소 비교
    base = days[0]
    for i in range(1, len(days)):
        if base >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            base = days[i] # 기준 갱신
            cnt = 1
    answer.append(cnt)
    return answer