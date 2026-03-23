import subprocess
from datetime import datetime, timedelta

TARGET_FILE = 'coding_test.md'
users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
data = {}

for u in users:
    remote_branch = f"origin/{u}"
    try:
        fs_out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', remote_branch]).decode('utf-8')
        files = [x for x in fs_out.split('\n') if x.startswith('백준/') or x.startswith('프로그래머스/')]
    except subprocess.CalledProcessError:
        continue

    for f in files:
        if 'Title:' not in f:
            continue
        try:
            log = subprocess.check_output(['git', 'log', '-1', '--format=%ad', '--date=iso', remote_branch, '--', f]).decode('utf-8').strip()
            if log:
                dt = datetime.strptime(log[:19], "%Y-%m-%d %H:%M:%S")
                if dt.hour == 0:
                    dt -= timedelta(days=1)
                
                # 테스트 목적으로 모든 요일의 데이터가 수집되도록 필터링 해제
                date_str = dt.strftime("%m-%d")
                if date_str not in data:
                    data[date_str] = {x: 0 for x in users}
                data[date_str][u] += 1
        except subprocess.CalledProcessError:
            pass

table_content = "| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
for k in sorted(data.keys(), reverse=True):
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

try:
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = ""
    end_marker = ""

    if start_marker in content and end_marker in content:
        # 정규표현식 오류를 원천 차단하기 위해 텍스트 절단 방식(.split) 채택
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[-1]
        
        new_content = before + start_marker + "\n" + table_content + end_marker + after
        
        with open(TARGET_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
except FileNotFoundError:
    pass
