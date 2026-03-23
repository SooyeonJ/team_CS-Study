import os, subprocess
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
                
                date_str = dt.strftime("%m-%d")
                if date_str not in data:
                    data[date_str] = {x: 0 for x in users}
                data[date_str][u] += 1
        except subprocess.CalledProcessError:
            pass

table_content = "| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
for k in sorted(data.keys(), reverse=True):
    dt_obj = datetime.strptime(f"{datetime.now().year}-{k}", "%Y-%m-%d")
    weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
    
    row = f"| {k} | {weekday_kr} |"
    for u in users:
        row += f" O ({data[k][u]}) |" if data[k][u] > 0 else " X |"
    table_content += row + "\n"

# 파일 및 마커 존재 여부를 사전에 검증하여 에러 원천 차단
if os.path.exists(TARGET_FILE):
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    s_mark = ""
    e_mark = ""

    if s_mark in content and e_mark in content:
        before = content.split(s_mark)[0]
        after = content.split(e_mark)[-1]
        with open(TARGET_FILE, 'w', encoding='utf-8') as f:
            f.write(before + s_mark + "\n" + table_content + e_mark + after)
    else:
        print(f"Warning: Markers not found in {TARGET_FILE}.")
else:
    print(f"Warning: {TARGET_FILE} not found.")
