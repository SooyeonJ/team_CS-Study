'counter 함수 이용'
from collections import Counter

def solution(topping):
    answer = 0
    
    left = set() #중복 제거를 위해 set으로 만들어줌
    right = Counter(topping) #right는 Counter로 만들어 토핑 개수 파악
    # 출력: Counter({'철수': 2, '영희': 2, '민수': 1})
    
    for t in topping:
        left.add(t) #left에 토핑 하나 추가
                    #.add()는 set 자료형에 새로운 원소를 추가할 때 사용하는 기본 메서드
        right[t]-=1 #right에서 해당 토핑 개수 -1
        
        #토핑을 옮긴 후 해당 토핑이 더 이상 right에 없으면 제거
        if right[t]==0:
            del right[t] #Counter는 내부적으로 딕셔너리 구조를 가진다. del을 사용하면 key(요소)와 value(빈도수)를 세트로 통째로 완전히 삭제한다. set에서 특정 원소를 지우고 싶을 때는 del 대신 .remove 전용 메서드를 사용해야 한다.
            
        
        if len(left) == len(right):
            answer+=1
    
    return answer
   
    

        