def solution(s):
    count=0
    
    if s[0]==')' or s[-1]=='(':
        return False
    for x in s:
        if x=='(':
            count+=1
        else:
            count-=1
        if count<0:
            return False
    
    if count==0:
        return True
    else:
        return False
        
                           
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
   