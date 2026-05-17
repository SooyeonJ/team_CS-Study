def anw(a):
    answer=[]
    for i in range(1,a+1):
        if a%i==0:
            answer.append(i)
    return len(answer)
    
def solution(left, right):
    
    result=[]
    for i in range(left,right+1):
        if(anw(i)%2==0):
            result.append(i)
        elif(anw(i)%2!=0):
            result.append(-i)
  
    return sum(result)
            
            
