def solution(order):
    answer = [x for x in str(order) if x=='3' or x=='6'or x=='9']
    return len(answer)