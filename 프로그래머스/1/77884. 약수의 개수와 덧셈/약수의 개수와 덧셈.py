def anw(a):
    count=0
    result=[]
    for x in range(1,a+1):
        if x*x==a:
            count+=1
        else:
            if a%x==0:
                count+=1
    return count
        

def solution(left,right):
    sol=[]
    for result in range(left,right+1):
        if anw(result)%2==0:
            sol.append(result)
        else: sol.append(-result)
    
    return sum(sol)
        
    

        
            
            
