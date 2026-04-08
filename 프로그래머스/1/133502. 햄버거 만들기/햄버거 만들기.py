def solution(ingredient):
    answer = 0
    stack = []
    
    for burger in ingredient:
        stack.append(burger)
        if len(stack)>3:
                if stack[-4:]==[1,2,3,1]:
                    del stack[-4:]
                    answer+=1
            
    return answer
    
