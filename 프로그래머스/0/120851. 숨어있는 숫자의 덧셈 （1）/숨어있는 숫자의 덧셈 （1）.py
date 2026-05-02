def solution(my_string):
    sum=0
    number = [int(x) for x in my_string if x.isdigit()]
    
    for n in number:
        sum+=n
    
    return sum 