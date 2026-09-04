def solution(s):
    stack=[]
    
    for char in s:
        if stack and char==stack[-1]:
            stack.pop(-1)
        elif len(stack)==0 or char!=stack[-1]:
            stack.append(char)
                        
    if len(stack)==0:
        return 1
    else: return 0
        

                
    
   