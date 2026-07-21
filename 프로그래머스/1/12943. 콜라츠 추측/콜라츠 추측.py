def solution(num):
    counter=0
    while num!=1:
        if counter>=500:
            num!=1
            return -1
        elif num%2==0:
            num=num//2
            counter+=1
        elif num%2!=0:
            num=num*3+1
            counter+=1
    return counter
        

        
    
            
            
            