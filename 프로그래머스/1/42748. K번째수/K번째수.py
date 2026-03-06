def solution(array, commands):
    answer = []
    for i, val in enumerate(commands):
        answer.append(sorted(array[val[0]-1:val[1]])[val[2]-1])
    return answer