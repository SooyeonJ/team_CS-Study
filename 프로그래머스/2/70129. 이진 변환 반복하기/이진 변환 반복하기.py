def solution(s):
    answer = []
    zero_cnt = 0
    cnt = 0
    while (s != '1'):
        zero_cnt += s.count(str(0))
        s = str(bin(len(s.replace('0', '')))).replace('0b', '')
        cnt += 1
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer