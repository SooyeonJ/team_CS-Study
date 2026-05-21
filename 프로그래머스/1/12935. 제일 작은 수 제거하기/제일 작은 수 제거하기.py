def solution(arr):
     
    min_value = min(arr)
    return [x for x in arr if x!=min_value] or [-1]