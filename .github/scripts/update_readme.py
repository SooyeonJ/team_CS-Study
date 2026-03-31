import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

# KST 환경 설정
env = os.environ.copy()
env['TZ'] = 'Asia/Seoul'

print("--- 데이터 수집 시작 ---")
for u in users:
    remote_branch = f"origin/{u}"
    try:
        # fetch --all 이후 최신 로그 수집
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%ad|%s', '--date=format-local:%Y-%m-%d %H:%M:%S', remote_branch], 
            stderr=subprocess.DEVNULL,
            env=env
        ).decode('utf-8').strip()
        
        if not logs_out:
            continue
            
        logs = logs_out.split('\n')
        print(f"User {u}: {len(logs)}개의 커밋 발견")
    except subprocess.CalledProcessError:
        print(f"User {u}: 브랜치를 찾을 수 없거나 로그 읽기 실패")
        continue

    for log in logs:
        if '|' not in log: continue
        dt_str, msg = log.split('|', 1)
        if 'Title:' not in msg: continue
            
        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")
            
            # 익일 1시 마감 및 월/수/금 선행 매핑
            adjusted_dt = dt - timedelta(hours=1)
            wd = adjusted_dt.weekday()
            
            # 다음 마감일 계산 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
            shift_days = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 2, 6: 1}
            target_dt = adjusted_dt + timedelta(days=shift_days[wd])
            
            month_key = target_dt.strftime("%Y-%m") 
            date_str = target_dt.strftime("%m-%d")  
            
            if month_key not in monthly_data:
                monthly_data[month_key] = {}
            if date_str not in monthly_data[month_key]:
                monthly_data[month_key][date_str] = {x: 0 for x in users}
            monthly_data[month_key][date_str][u] += 1
        except Exception:
            pass

print("--- 파일 업데이트 시작 ---")
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

        # [수정] 요청하신 새로운 종료 마커 적용
        s_mark = "## 코딩테스트 진행 과정"
        e_mark = "## 💰 벌금 예외 사항"

        if s_mark in content and e_mark in content:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
            print(f"Success: {target_file} 업데이트 완료")
        else:
            print(f"Warning: {target_file} 내 마커 불일치 ({s_mark} 또는 {e_mark} 누락)")
    else:
        print(f"Warning: {target_file} 파일 없음, 스킵")
