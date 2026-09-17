def solution(numbers):
    result=[]
    for i,x in enumerate(numbers):
        for y in numbers[i+1:len(numbers)]:
            result.append(x+y)
            
    return sorted(set(result))