
from itertools import permutations
def solution(numbers):
    num_arr = []
    result = []
    numbers = list(numbers) 
    
    for i in range(len(numbers)+1):
        for j in permutations(numbers, i):
            if (len(list(j)) > 0) and (list(j)[0] != '0'): 
                num_arr.append(''.join((list(j))))
    num_arr = list(set(num_arr))
        
    # 소수 판별    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

    for x in num_arr:
        if is_prime(int(x)):     # 소수 판별
            result.append(int(x))
    return len(result)