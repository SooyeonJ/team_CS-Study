def solution(data, ext, val_ext, sort_by):
    arr = []
    answer = []
    # ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    idx_map = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for i, val in enumerate(data):
        if val[idx_map[ext]] < val_ext:
            arr.append(val)

    answer = sorted(arr, key=lambda x: x[idx_map[sort_by]])
    return answer
