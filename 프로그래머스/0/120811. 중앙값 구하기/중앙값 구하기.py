def solution(array):
    array.sort()
    mid = (1+len(array))//2
    return array[mid-1]
    