def solution(n):
    
    '파이썬에서 count()는 주로 문자열과 리스트/튜플에서 사용된다.'
    '10진수로 변환해주는 형식 int(문자열 or 리터럴, 현재의 진수)'
    binary = bin(n).count('1')
    'while 안에서 n+1 해주면 값이 계속 리셋됨'
    current=n
    while True:
        current+=1
        if bin(current).count('1')==binary:
            return current
    
    
        
            
    