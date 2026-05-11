def solution(quiz):
    rresult=[]
    result=0
    for x in quiz:
        answer = x.split()
        if(answer[1] == '-'):
            result = int(answer[0])-int(answer[2])
            if(int(answer[4])==result):
                    rresult.append('O')
            else:
                    rresult.append('X')
        elif(answer[1] == '+'):
            result = int(answer[0])+int(answer[2])
            if(int(answer[4])==result):
                    rresult.append('O')
            else:
                    rresult.append('X')
            
    return rresult
        
    
        
    
        
                
                
                
                
                
    