def solution(sizes):
    arr_w = []
    arr_h = []
    for i in sizes:
        arr_w.append(sorted(i)[0])
        arr_h.append(sorted(i)[1])
    return max(sorted(arr_w)) * max(sorted(arr_h))