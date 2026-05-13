def solution(array, commands):
    answer = []
    result = []
    for com in commands:
        answer=array[com[0]-1:com[1]:1]
        answer.sort()
        result.append(answer[com[2]-1])
    return result
    