from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    else:
        for x in range(2,int(n**0.5)+1):
            if n%x==0:
                return False
        return True
        
def solution(numbers):
    
    target=[]
    for x in range(1,len(numbers)+1):
        for y in permutations(numbers,x):
            if is_prime(int(''.join(y)))==True:
                target.append(int(''.join(y)))
    'del 리스트[] : 인덱스나 범위 지정 삭제(삭제하려는 요소의 위치를 알고있어야함)'
    'remove() : 값으로 삭제, 삭제하려는 값 자체를 알고있어야함, 리스트에 없는 값을 넣으면 ValueError 발생'
    'pop() : 삭제 후 값 가져오기, 요소를 삭제함과 동시에 삭제된 값을 변수에 담아 활용하고 싶을 때 사용'
    return len(set(target))
    
    
   