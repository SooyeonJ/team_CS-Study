def solution(n, m, section):
    '그리디 알고리즘 : 매 순간 가정 최적이라고 생각되는 선택을 해나가는 방식'
    answer = 0
    painted_until = 0 # 어디까지 칠해졌는지 나타냄
    
    for s in section:
        if s > painted_until:
            answer+=1
            painted_until=s+m-1
    
    return answer
    