def solution(price, money, count):
    
    total=0
    for x in range(1,count+1):
        total+=price*x
        
    if total-money>0:
        return total-money
    elif total-money<=0:
        return 0