def solution(citations):
    '''
    H-Index는 내림차순 정렬하여 인용수>=논문수
    논문수보다 인용수가 작아지면, 인용수가 n번째 이상인
    논문수가 최소 n개 이상인 논문 수가 몇 개 이상 있다고
    말할 수 없다.
    '''
    citations.sort(reverse=True)
    
    for x in citations:
        if x!=0:
            return max([i+1 for i,x in enumerate(citations) if i+1<=x]) 
        else:
            return 0
    
    
    