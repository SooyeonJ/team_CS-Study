def solution(people, limit):
    '최대 2명 조건(투 포인터 방법으로 풀어야함)'
    '가장 무거운 사람 1명 기준으로 생각'
    people.sort()
    left=0
    right=len(people)-1
    boats=0
    
    while left<=right:
        '가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 있는 경우'
        if people[left]+people[right]<=limit:
            '가장 가벼운 사람 탑승'
            left+=1
            
            '무거운 사람은 무조건 탑승(기준)'
        right-=1
        boats+=1
            
    return boats

