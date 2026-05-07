def solution(my_string):
    answer=[]
    for x in my_string:
        if x.islower() == True:
            answer.append(x.upper())
        elif x.isupper() == True:
            answer.append(x.lower())
    return ''.join(answer)

