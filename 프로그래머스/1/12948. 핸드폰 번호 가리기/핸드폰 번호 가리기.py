def solution(phone_number):
    
    
    return ''.join(list(map(lambda x:'*',phone_number[:len(phone_number)-4:]))+list(phone_number[len(phone_number)-4:len(phone_number):]))