def solution(d, budget):
    answer = 0
    for i in sorted(d):
        # print(budget, i, 'cnt =', answer)
        budget -= i
        if (budget >= 0):
            answer += 1
    return answer