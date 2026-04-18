def solution(n):
    arr = [i for i in range(1, n) if n % i == 1]
    return min(arr)