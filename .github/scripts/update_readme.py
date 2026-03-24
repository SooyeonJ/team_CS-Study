import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

# 데이터 수집 및 월별 그룹화
for u in users:
    remote_branch = f"origin/{u}"
    try:
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%ad|%s', '--date=iso', remote_branch, '--', '백준', '프로그래머스'], 
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
        
        if not logs_out:
            continue
            
        logs = logs_out.split('\n')
    except subprocess.CalledProcessError:
        continue

    for log in logs:
        if '|' not in log:
            continue
        dt_str, msg = log.split('|', 1)
        
        if 'Title:' not in msg:
            continue
            
        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")
            
            adjusted_dt = dt - timedelta(hours=1)
            wd = adjusted_dt.weekday()
            
            shift_days = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 2, 6: 1}
            target_dt = adjusted_dt + timedelta(days=shift_days[wd])
            
            # 연-월(YYYY-MM)을 추출하여 파일명 기준으로 사용
            month_key = target_dt.strftime("%Y-%m") 
            date_str = target_dt.strftime("%m-%d")  
            
            if month_key not in monthly_data:
                monthly_data[month_key] = {}
            if date_str not in monthly_data[month_key]:
                monthly_data[month_key][date_str] = {x: 0 for x in users}
            monthly_data[month_key][date_str][u] += 1
        except Exception:
            pass

# 월별로 독립된 마크다운 파일 업데이트 진행
for month_key, data in monthly_data.items():
    target_file = f"{month_key}.md"
    
    table_content = "\n\n| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
    for k in sorted(data.keys(), reverse=True):
        dt_obj = datetime.strptime(f"{month_key[:4]}-{k}", "%Y-%m-%d")
        weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
        
        row = f"| {k} | {weekday_kr} |"
        for u in users:
            row += f" O ({data[k][u]}) |" if data[k][u] > 0 else " X |"
        table_content += row + "\n"
    table_content += "\n"

    if os.path.exists(target_file):
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 월별 파일에 적용될 파싱 구분자 지정
        s_mark = "## 코딩테스트 진행 과정"
        e_mark = "## 한 줄 회고"

        if s_mark in content and e_mark in content:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
        else:
            print(f"Warning: {target_file} 파일 내에 구분자 헤더가 없습니다.")
    else:
        print(f"Warning: {target_file} 파일이 존재하지 않아 건너뜁니다.")
