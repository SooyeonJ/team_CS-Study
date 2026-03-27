def solution(priorities, location):
    queue = []
    for i in range(len(priorities)):
        queue.append((priorities[i], i)) # (중요도, 원래위치) 형태로 변환
    count = 0  # 몇 번째로 출력되는지

    # 큐가 빌 때까지 반복
    while len(queue) > 0:
        cur = queue.pop(0)  
        # 뒤에 더 큰 중요도가 있는지 확인
        flag = False
        for q in queue:
            # q도 (중요도, 위치) 튜플
            if cur[0] < q[0]:
                flag = True
                break
        # 더 큰 값이 있으면 → 뒤로 보냄
        if flag == True:
            queue.append(cur)
        else:
            count += 1
            if cur[1] == location:
                return count