def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if arr1[i % len(arr1)] == answers[i]:
            cnt1 += 1
        if arr2[i % len(arr2)] == answers[i]:
            cnt2 += 1
        if arr3[i % len(arr3)] == answers[i]:
            cnt3 += 1           
        
    max_score = max(cnt1, cnt2, cnt3)
    if cnt1 == max_score:
        answer.append(1)
    if cnt2 == max_score:
        answer.append(2)
    if cnt3 == max_score:
        answer.append(3)
    
    return answer