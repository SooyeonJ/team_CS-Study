def solution(new_id):
    
    
    new_id = new_id.lower()
    answer=''
    for x in new_id:
        if x.isalnum() or x in '-_.':
            answer+=x
    
    while '..' in answer:
        answer=answer.replace('..','.')
            
    answer=answer.strip('.')
       
    if not answer:
        answer='a'
        
    if len(answer)>=16:
        answer=answer[:15].rstrip('.')
    while(len(answer)<=2):
        answer+=answer[-1]
        
    return answer
        
        
