def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack=[]
    for i in arr:
        if not stack or stack[-1]!=i:
            stack.append(i)
            
    return stack
    
        
 