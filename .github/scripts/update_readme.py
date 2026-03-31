import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

env = os.environ.copy()
env['TZ'] = 'Asia/Seoul'

print("--- [디버깅 모드] 커밋 데이터 상세 분석 ---")
for u in users:
    remote_branch = f"origin/{u}"
    try:
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%ad|%s', '--date=format-local:%Y-%m-%d %H:%M:%S', remote_branch], 
            stderr=subprocess.DEVNULL, env=env
        ).decode('utf-8').strip()
        
        if not logs_out: continue
        logs = logs_out.split('\n')
    except Exception as e:
        print(f"Error: {u} 브랜치 접근 실패")
        continue

    for log in logs:
        if '|' not in log: continue
        dt_str, msg = log.split('|', 1)
        
        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")
            
            # 최근 3일(3월 28일 이후)의 커밋만 필터링하여 로그에 출력
            if dt > datetime(2026, 3, 28):
                print(f"[{u}] 시간: {dt_str[:19]} | 메시지: {msg}")
                
                if 'Title:' not in msg:
                    print(f"  -> ❌ 거절됨: 'Title:' 키워드가 메시지에 없습니다.")
                    continue
                    
                adjusted_dt = dt - timedelta(hours=1)
                wd = adjusted_dt.weekday()
                shift_days = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 2, 6: 1}
                target_dt = adjusted_dt + timedelta(days=shift_days[wd])
                
                month_key = target_dt.strftime("%Y-%m") 
                date_str = target_dt.strftime("%m-%d")  
                
                print(f"  -> ✅ 승인됨: 타겟 마감일 [{date_str}] 표에 집계됩니다.")
                
                if month_key not in monthly_data:
                    monthly_data[month_key] = {}
                if date_str not in monthly_data[month_key]:
                    monthly_data[month_key][date_str] = {x: 0 for x in users}
                monthly_data[month_key][date_str][u] += 1
        except Exception as e:
            pass

print("\n--- 파일 업데이트 시작 ---")
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

        s_mark = "## 코딩테스트 진행 과정"
        e_mark = "## 💰 벌금 예외 사항"

        if s_mark in content and e_mark in content:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
        else:
            pass
