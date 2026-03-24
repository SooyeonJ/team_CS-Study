import os, subprocess
from datetime import datetime, timedelta

TARGET_FILE = 'coding_test.md'
users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
data = {}

# 데이터 수집 (개별 파일 탐색 -> 커밋 로그 단위 탐색으로 변경)
for u in users:
    remote_branch = f"origin/{u}"
    try:
        # 백준, 프로그래머스 폴더에서 발생한 커밋 전체를 추출 (형식: 날짜|커밋메시지)
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%ad|%s', '--date=iso', remote_branch, '--', '백준', '프로그래머스'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        
        if not logs_out:
            continue
            
        logs = logs_out.split('\n')
    except subprocess.CalledProcessError:
        continue

    # 추출된 커밋 로그 분석
    for log in logs:
        if '|' not in log:
            continue
        dt_str, msg = log.split('|', 1)
        
        # 커밋 메시지에 백준허브 고유 키워드인 'Title:'이 있는 경우만 문제 풀이로 인정
        if 'Title:' not in msg:
            continue
            
        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")
            
            # 익일 1시 마감 보정 및 월/수/금 선행 매핑 로직
            adjusted_dt = dt - timedelta(hours=1)
            wd = adjusted_dt.weekday()
            
            shift_days = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 2, 6: 1}
            target_dt = adjusted_dt + timedelta(days=shift_days[wd])
            
            date_str = target_dt.strftime("%m-%d")
            
            if date_str not in data:
                data[date_str] = {x: 0 for x in users}
            data[date_str][u] += 1
        except Exception:
            pass

# 마크다운 표 생성
table_content = "\n\n| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
for k in sorted(data.keys(), reverse=True):
    dt_obj = datetime.strptime(f"{datetime.now().year}-{k}", "%Y-%m-%d")
    weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
    
    row = f"| {k} | {weekday_kr} |"
    for u in users:
        row += f" O ({data[k][u]}) |" if data[k][u] > 0 else " X |"
    table_content += row + "\n"
table_content += "\n"

# 파일 업데이트
if os.path.exists(TARGET_FILE):
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    s_mark = "# 코딩테스트 진행 과정"
    e_mark = "# 📆 문제 일정 (고득점 Kit 기준)"

    if s_mark in content and e_mark in content:
        before = content.split(s_mark)[0]
        after = content.split(e_mark)[-1]
        
        with open(TARGET_FILE, 'w', encoding='utf-8') as f:
            f.write(before + s_mark + table_content + e_mark + after)
    else:
        print(f"Error: {TARGET_FILE} 파일 내에 '{s_mark}' 또는 '{e_mark}' 헤더가 없습니다.")
else:
    print(f"Error: {TARGET_FILE} 파일을 찾을 수 없습니다.")
