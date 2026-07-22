def solution(strings, n):
    
    'lambda 앞에 key=를 써줘야 하는 이유, key를 쓰지 않으면 lambda를 데이터로 인식해서 에러, key는 reverse처럼 정렬 기준을 정해주는 옵션'
    'lambda x:(반환할 표현식)'
    'sorted(strings, reverse=True), sorted(strings, key=lambda x: (x[n], x), reverse=True)'
    return sorted(strings,key=lambda x:(x[n],x))
            
          
    
    

    