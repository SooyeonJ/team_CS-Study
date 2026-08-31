'''
lv1.num이 1이면 0반환
lv1.num이 1이 아니면
  lv2.num이 짝수일때
  lv2.num이 홀수일때
  lv2. answer += 1
  lv2. answer > 500일때 -1반환
'''
def solution(num):
    answer = 0
    if num == 1: return 0
    while (num != 1):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer > 500: return -1
    return answer