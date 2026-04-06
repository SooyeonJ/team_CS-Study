def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)    
    return str(int(''.join(numbers))) # 앞에 0 여러 개 나오면 하나로 줄여야 함