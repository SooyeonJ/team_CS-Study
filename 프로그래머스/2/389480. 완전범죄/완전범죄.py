def solution(info, n, m):
    INF = 10**9
    # dp[b] = B 흔적 합이 b일 때 가능한 A 흔적 합의 최솟값
    dp = [INF] * m
    dp[0] = 0

    for a, b in info:
        ndp = [INF] * m
        for bs in range(m):
            if dp[bs] == INF:
                continue

            # 1) 이번 물건을 A가 훔침
            na = dp[bs] + a
            if na < n:
                if na < ndp[bs]:
                    ndp[bs] = na

            # 2) 이번 물건을 B가 훔침
            nb = bs + b
            if nb < m:
                if dp[bs] < ndp[nb]:
                    ndp[nb] = dp[bs]

        dp = ndp

    ans = min(dp)
    return -1 if ans == INF else ans
