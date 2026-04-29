def solution(people, limit):
    answer = 0
    # 1. 몸무게를 오름차순으로 정렬
    people.sort() 
    
    # 양 끝을 가리키는 두 개의 포인터 설정
    left = 0 
    right = len(people) - 1 
    
    # 포인터가 교차하기 전까지(모든 사람을 검사할 때까지) 반복
    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 <= 제한 무게
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 구출 완료 (오른쪽으로 한 칸 이동)
            right -= 1 # 무거운 사람 구출 완료 (왼쪽으로 한 칸 이동)
        # 제한 무게 초과 시 무거운 사람만 탑승
        else:
            right -= 1 # 무거운 사람 혼자 구출 완료 (왼쪽으로 한 칸 이동)
            
        # 짝을 지었든 혼자 탔든, 보트는 1대 출발함
        answer += 1
        
    return answer