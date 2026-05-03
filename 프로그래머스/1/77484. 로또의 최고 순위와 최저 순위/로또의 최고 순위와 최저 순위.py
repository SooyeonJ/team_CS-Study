from collections import Counter

def solution(lottos, win_nums):
    answer = []
    rcnt = 0
    hcnt = 0
    
    for i in lottos:
        if i in win_nums:
            rcnt += 1;
    hcnt = rcnt + Counter(lottos)[0]
    
    # 함수로 구현
    def get_grade(cnt):
        if cnt == 6: return 1
        elif cnt == 5: return 2
        elif cnt == 4: return 3
        elif cnt == 3: return 4
        elif cnt == 2: return 5
        else: return 6
    
    answer.append(get_grade(hcnt))  # 최고 순위
    answer.append(get_grade(rcnt))  # 최저 순위
        
    return answer
