def solution(phone_book):
    answer = True
    phone_books = sorted(phone_book)
    for i in range(len(phone_books)-1):
        if phone_books[i+1].startswith(phone_books[i]):            
            answer = False
    return answer