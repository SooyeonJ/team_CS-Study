def solution(brown, yellow):
    
    '카펫 가로>=세로'
    '1. return의 곱(w,h)은 b+y와 같다'
    '2. return w,h 값이 한 칸의 w,h가 아니라 전체 w,h이다.'
    'total은 전체 넓이가 아니라, 전체 개수이다. 즉, total=b+y or w*h'
    total=brown+yellow
    '여기서 for은 h 값을 구하는 거니깐 변수가 h가 되는 게 계산이 편하다'
    'yellow의 개수는 brownd의 양변 모서리를 하나씩 뺀 y==(w-2)*(h-2)'
    '즉, 그래서 h가 3보다 커야한다.'
    for h in range(3,total):
        if total%h==0:
            w=total//h
            if yellow==(w-2)*(h-2):
                return [w,h]
            
    
    