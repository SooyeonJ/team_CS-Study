'''
lv1. 배열 돌면서
  lv2. 카운트 초기화 
  lv2. 1일때까지 반복
    lv3. 짝수일때
    lv3. 홀수일때
    lv3. 카운트 누적
  lv2. answer 누적
  lv2. result에 누적
'''
def solution(num_list):
    answer = 0
    for i in num_list:
        cnt = 0
        while (i != 1):
            if (i % 2 == 0):
                i = i / 2
            else:
                i = (i-1) / 2
            cnt += 1
        answer += cnt
    return answer