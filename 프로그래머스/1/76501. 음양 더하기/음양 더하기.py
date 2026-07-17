def solution(absolutes, signs):
    
    '''
    return sum(absolutes)-2*sum([x for i,x in enumerate(absolutes) if signs[i]==False])
    '''
    
    return sum(absolutes)+2*sum([-x for x,i in zip(absolutes,signs) if i==False])