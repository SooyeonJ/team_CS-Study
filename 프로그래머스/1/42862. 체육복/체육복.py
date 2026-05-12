def solution(n, lost, reserve):
    total = [1]*(n+2)
    
    for i in reserve:
        total[i]+=1
    for i in lost:
        total[i]-=1
    
    for i in range(1,n+1):
        if(total[i]==0):
            if(total[i-1]==2):
                total[i]+=1
                total[i-1]-=1
            elif(total[i+1]==2):
                total[i]+=1
                total[i+1]-=1

    answer=0
    for i in range(1,n+1):
        if(total[i]>0):
            answer+=1
            
    return answer
            
            
            