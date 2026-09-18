def solution(progresses, speeds):
    '''
    남은 작업량 계산하는 방법
    - 남은 작업량 : 100 - progress
    - 하루 작업 속도 : speed
    - 필요한 일수 : 남은 작업량 / 하루 작업 속도
        (만약에 % !=0 이면 올림 처리한다.)
    '''
    stack = [1]
    remain = 100 - progresses[0]
    day = remain//speeds[0]  if remain%speeds[0] == 0 else (remain//speeds[0] + 1)
    for i in range(1,len(progresses)):
        if (100 - progresses[i])/speeds[i]<=day:
            stack[-1]+=1
        else:
            stack.append(1)
            remain=100 - progresses[i]
            day = remain//speeds[i]  if remain%speeds[i] == 0 else (remain//speeds[i] + 1)
            
    return stack
            
    
    
        
    
        
            
    
            
            
    
    
        
            