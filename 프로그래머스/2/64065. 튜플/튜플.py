def solution(s):
    
    s=s[2:-2].split('},{')
    x=[set(map(int,i.split(','))) for i in s]
    'sort 함수에 길이 함수를 계산해서 오름차순 정렬하고 싶으면 key=len을 넣어준다'
    x.sort(key=len)
    
    answer = []
    seen = set()
    
    for current in x:
        '현재 집합에서 이미 찾은 원소 seen을 뺀 나머지 원소찾기'
        sol=list(current-seen)[0]
        answer.append(sol)
        seen.add(sol)
        
        
    return answer
    
        
        
        
    
        

 