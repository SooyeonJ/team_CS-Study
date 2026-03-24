import os, subprocess
from datetime import datetime, timedelta

TARGET_FILE = 'coding_test.md'
users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
data = {}

for u in users:
    remote_branch = f"origin/{u}"
    try:
        fs_out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', remote_branch], stderr=subprocess.DEVNULL).decode('utf-8')
        files = [x for x in fs_out.split('\n') if x.startswith('백준/') or x.startswith('프로그래머스/')]
    except subprocess.CalledProcessError:
        continue

    for f in files:
        if 'Title:' not in f:
            continue
        try:
            log = subprocess.check_output(['git', 'log', '-1', '--format=%ad', '--date=iso', remote_branch, '--', f], stderr=subprocess.DEVNULL).decode('utf-8').strip()
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

table_content = "\n\n| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
for k in sorted(data.keys(), reverse=True):
    dt_obj = datetime.strptime(f"{datetime.now().year}-{k}", "%Y-%m-%d")
    weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
    
    row = f"| {k} | {weekday_kr} |"
    for u in users:
        row += f" O ({data[k][u]}) |" if data[k][u] > 0 else " X |"
    table_content += row + "\n"
table_content += "\n"

if os.path.exists(TARGET_FILE):
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # 눈에 보이지 않는 주석 대신 마크다운에 작성된 제목 텍스트를 직접 구분자로 사용
    s_mark = "# 코딩테스트 진행 과정"
    e_mark = "# 📆 문제 일정 (고득점 Kit 기준)"

    if s_mark in content and e_mark in content:
        before = content.split(s_mark)[0]
        after = content.split(e_mark)[-1]
        
        # 파일 덮어쓰기
        with open(TARGET_FILE, 'w', encoding='utf-8') as f:
            f.write(before + s_mark + table_content + e_mark + after)
    else:
        print(f"Error: {TARGET_FILE} 파일 내에 '{s_mark}' 또는 '{e_mark}' 헤더가 없습니다.")
else:
    print(f"Error: {TARGET_FILE} 파일을 찾을 수 없습니다.")
