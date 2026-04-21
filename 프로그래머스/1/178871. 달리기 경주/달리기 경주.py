def solution(players, callings):
    pos = {}

    for i, name in enumerate(players):
        pos[name] = i
    for name in callings:
        now = pos[name]          # 현재 위치
        front = players[now - 1] # 앞 사람
        players[now - 1], players[now] = players[now], players[now - 1]

        # 딕셔너리 위치도 같이 바꾸기
        pos[name] = now - 1
        pos[front] = now

    return players