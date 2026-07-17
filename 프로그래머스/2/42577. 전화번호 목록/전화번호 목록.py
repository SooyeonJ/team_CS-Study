def solution(phone_book):
    
    '''
    효율성에서 오류가 난 이유
    전화번호 길이가 1,000,000인데 이를 2중
    for문해서 파이썬의 연산이 길어진다.
    sort()를 하게 되면, 접두어 관계인 문자열들은
    앞뒤로 나란히 위치하기 때문에
    2중 for문이 아닌 한바퀴만 돌아도 시간 복잡도가 
    줄어든다.
    phone_book.sort()
    for x in phone_book:
        for y in phone_book:
            if x!=y:
                if x==y[0:len(x)]:
                        return False
            
    return True
    '''    
        
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): 
            return False
    
    return True
    