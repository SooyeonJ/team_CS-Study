def solution(my_string):

    number = [int(x) for x in my_string if x.isdigit()]
    
    return sum(number)