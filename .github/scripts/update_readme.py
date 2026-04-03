import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

# 깃허브 액션 환경의 타임존을 한국 표준시(KST)로 일치시킴
env = os.environ.copy()
env['TZ'] = 'Asia/Seoul'

for u in users:
    remote_branch = f"origin/{u}"
    try:
        # 모든 커밋 로그 수집
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%ad|%s', '--date=format-local:%Y-%m-%d %H:%M:%S', remote_branch], 
            stderr=subprocess.DEVNULL, env=env
        ).decode('utf-8').strip()
        
        if not logs_out: continue
        logs = logs_out.split('\n')
    except Exception:
        continue

    for log in logs:
        if '|' not in log: continue
        dt_str, msg = log.split('|', 1)
        
        # 백준허브 식별자 확인
        if 'Title:' not in msg: continue
            
        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")
            
            # 익일 오전 1시 마감 기준 처리 (오전 1시 이전 커밋은 전날 기록으로 인정)
            # 매일 업데이트를 위해 shift_days 로직 제거
            target_dt = dt - timedelta(hours=1)
            
            month_key = target_dt.strftime("%Y-%m") 
            date_str = target_dt.strftime("%m-%d")  
            
            if month_key not in monthly_data:
                monthly_data[month_key] = {}
            if date_str not in monthly_data[month_key]:
                monthly_data[month_key][date_str] = {x: 0 for x in users}
            monthly_data[month_key][date_str][u] += 1
        except Exception:
            pass

for month_key, data in monthly_data.items():
    target_file = f"{month_key}.md"
    
    table_content = "\n\n| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
    # 날짜별로 내림차순 정렬하여 테이블 생성
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

        s_mark = "## 코딩테스트 진행 과정"
        e_mark = "## 💰 벌금 예외 사항"

        if s_mark in content and e_mark in content:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
