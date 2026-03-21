def solution(phone_book):
    hash_map={}
    
    for num in phone_book:
        hash_map[num]=1
    
    for number in phone_book:
        tp=""
        for cha in number:
            tp+=cha
            
            if tp in hash_map and tp!=number:
                return False
       
    
    answer = True
    return answer