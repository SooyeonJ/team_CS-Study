def solution(arr):
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack=[]
    
    for num in arr:
        if len(stack)==0 or stack[-1]!=num:
            stack.append(num)
            
    return stack