def solution(numbers):
    result = ''.join(sorted(map(str, numbers), key=lambda x: x*4, reverse=True))
    if result[0] == '0':
        return '0'
    return result