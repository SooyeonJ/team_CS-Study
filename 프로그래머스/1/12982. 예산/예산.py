def solution(d, budget):
    d = sorted(d)[::-1]
    arr = []
    if budget >= sum(d):
            return len(d)
    else:
        for i, val in enumerate(d):
            if budget >= sum(d[i+1:]):
                arr.append(len(d[i+1:]))
        return max(arr)
    