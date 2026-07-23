def solution(answers):
    giveUp1=[1,2,3,4,5]*len(answers)
    giveUp2=[2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    giveUp3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    
    count=[0,0,0]
    for x1,x2,x3,y in zip(giveUp1,giveUp2,giveUp3,answers):
        if x1==y:
            count[0]+=1
        if x2==y:
            count[1]+=1
        if x3==y:
            count[2]+=1
    
    return [i+1 for i,result in enumerate(count) if result==max(count)]
        
        
        
        
