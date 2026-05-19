def solution(num):
    
    count=0
    while num>0:
        if(num%2==0):
            num=num//2
            count+=1
        elif(num%2!=0):
            if(num==1):
                return count
            else:
                num=num*3+1
                count+=1
        if(count>=500):
            return -1
            break
            
            