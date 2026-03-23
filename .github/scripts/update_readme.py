import os, re, subprocess
from datetime import datetime, timedelta

# 타겟 파일명 전역 변수 설정
TARGET_FILE = 'coding_test.md'
users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
data = {}

for u in users:
    remote_branch = f"origin/{u}"
    try:
        # 원격 브랜치 파일 목록 조회
        fs_out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', remote_branch]).decode('utf-8')
        files = [x for x in fs_out.split('\n') if x.startswith('백준/') or x.startswith('프로그래머스/')]
    except subprocess.CalledProcessError:
        continue

    for f in files:
        if not re.search(r'\[(.*?)\] Title: (.*?),', f):
            continue
        try:
            # 커밋 로그 추출 (날짜 및 시간)
            log = subprocess.check_output(['git', 'log', '-1', '--format=%ad', '--date=iso', remote_branch, '--', f]).decode('utf-8').strip()
            if log:
                dt = datetime.strptime(log[:19], "%Y-%m-%d %H:%M:%S")
                
                # 익일 오전 1시(00:00 ~ 00:59) 제출분은 전날로 산정
                if dt.hour == 0:
                    dt -= timedelta(days=1)
                
                # 월(0), 수(2), 금(4)요일 제출분만 필터링
                if dt.weekday() not in [0, 2, 4]:
                    continue
                
                date_str = dt.strftime("%m-%d")
                if date_str not in data:
                    data[date_str] = {x: 0 for x in users}
                data[date_str][u] += 1
        except subprocess.CalledProcessError:
            pass

# 마크다운 표 생성
table_content = "| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
for k in sorted(data.keys(), reverse=True):
    # 연도를 현재 연도로 계산하여 요일 매핑 (스터디 시작 연도 기준)
    current_year = datetime.now().year
    dt_obj = datetime.strptime(f"{current_year}-{k}", "%Y-%m-%d")
    weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
    
    row = f"| {k} | {weekday_kr} |"
    for u in users:
        if data[k][u] > 0:
            row += f" O ({data[k][u]}) |"
        else:
            row += " X |"
    table_content += row + "\n"

# 타겟 파일 읽기 및 내용 갱신
try:
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'.*?',
        f'\n{table_content}',
        content,
        flags=re.DOTALL
    )
    
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
except FileNotFoundError:
    print(f"Error: {TARGET_FILE} 파일을 찾을 수 없습니다.")
