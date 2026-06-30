import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

# 깃허브 액션 환경의 타임존을 한국 표준시(KST)로 일치시킴
env = os.environ.copy()
env['TZ'] = 'Asia/Seoul'

def get_category(commit_hash):
    # 커밋된 파일 확장자로 SQL/알고리즘을 명확히 구분
    try:
        # -c core.quotepath=false 옵션을 추가하여 한글 파일명이 따옴표로 묶이는 것을 방지
        out = subprocess.check_output(
            ['git', '-c', 'core.quotepath=false', 'diff-tree', '--no-commit-id', '-r', '--name-only', commit_hash],
            stderr=subprocess.PIPE, env=env
        )
        
        # errors='ignore'를 추가하여 디코딩 에러로 스크립트가 터지는 것을 방지
        files = out.decode('utf-8', errors='ignore').strip().split('\n')

        algo_extensions = ('.py', '.java', '.cpp', '.js', '.c', '.cs')

        for f in files:
            # 양끝 공백 및 혹시 모를 쌍따옴표 제거 후 소문자 변환
            f_lower = f.strip().strip('"').lower() 
            if f_lower.endswith('.sql'):
                return 'SQL'
            elif f_lower.endswith(algo_extensions):
                return '알고리즘'
                
    except subprocess.CalledProcessError as e:
        print(f"  [에러] Git 명령어 실패: {e.stderr.decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"  [에러] 파이썬 처리 실패: {e}")
        
    return None

for u in users:
    remote_branch = f"origin/{u}"
    print(f"\n--- [{u}] 사용자 브랜치({remote_branch}) 확인 시작 ---")
    try:
        logs_out = subprocess.check_output(
            ['git', 'log', '--format=%H|%ad|%s', '--date=format-local:%Y-%m-%d %H:%M:%S', remote_branch],
            stderr=subprocess.DEVNULL, env=env
        ).decode('utf-8').strip()

        if not logs_out:
            print(f"[{u}] 커밋 내역이 비어있습니다.")
            continue
        logs = logs_out.split('\n')
        print(f"[{u}] 총 {len(logs)}개의 커밋 발견")
    except Exception as e:
        print(f"[{u}] 브랜치 접근 실패: 해당 이름의 브랜치가 없거나 git log 에러 발생")
        continue

    for log in logs:
        if '|' not in log:
            continue
        parts = log.split('|', 2)
        if len(parts) < 3:
            continue
        commit_hash, dt_str, msg = parts

        # 백준허브 식별자 확인
        if 'Title:' not in msg:
            continue

        try:
            dt = datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S")

            # 익일 오전 1시 마감 기준 처리
            target_dt = dt - timedelta(hours=1)

            month_key = target_dt.strftime("%Y-%m")
            date_str = target_dt.strftime("%m-%d")

            category = get_category(commit_hash)

            if category:
                print(f"  -> 유효 데이터 추가: {dt_str} | {category}")
                if month_key not in monthly_data:
                    monthly_data[month_key] = {}
                if date_str not in monthly_data[month_key]:
                    monthly_data[month_key][date_str] = {x: {'SQL': 0, '알고리즘': 0} for x in users}

                monthly_data[month_key][date_str][u][category] += 1
        except Exception:
            pass

for month_key, data in monthly_data.items():
    target_file = f"{month_key}.md"
    
    table_content = "\n\n| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
    for k in sorted(data.keys(), reverse=True):
        dt_obj = datetime.strptime(f"{month_key[:4]}-{k}", "%Y-%m-%d")
        weekday_kr = ["월", "화", "수", "목", "금", "토", "일"][dt_obj.weekday()]
        row = f"| {k} | {weekday_kr} |"
        for u in users:
            sql_cnt = data[k][u]['SQL']
            alg_cnt = data[k][u]['알고리즘']
            total = sql_cnt + alg_cnt
            if total == 0:
                row += " X |"
            else:
                parts = []
                if alg_cnt > 0:
                    parts.append(f"알고리즘({alg_cnt})")
                if sql_cnt > 0:
                    parts.append(f"SQL({sql_cnt})")
                row += f" O ({', '.join(parts)}) |"
        table_content += row + "\n"
    table_content += "\n"

    s_mark = "## 코딩테스트 진행 과정"
    e_mark = "## 💰 벌금 예외 사항"

    if os.path.exists(target_file):
        print(f"\n--- [{target_file}] 갱신 시도 ---")
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        has_s = s_mark in content
        has_e = e_mark in content
        
        if has_s and has_e:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
            print(f"[{target_file}] 표 업데이트 및 저장 완료!")
        else:
            print(f"업데이트 실패: 파일 내 기준 문자열이 정확히 일치하지 않습니다.")
            print(f" - '{s_mark}' 존재 여부: {has_s}")
            print(f" - '{e_mark}' 존재 여부: {has_e}")
            print("해결 방법: 마크다운 파일의 제목 띄어쓰기와 이모티콘을 위 문자열과 똑같이 맞춰주세요.")
    else:
        year_str, month_str = month_key.split('-')
        # 삼중 따옴표 에러 방지를 위해 이스케이프 문자(\n)를 사용한 단일 문자열로 처리
        template_content = f"# {year_str}년 {month_str}월 코딩테스트 현황\n\n{s_mark}{table_content}{e_mark}\n- 벌금 면제자 및 사유를 이곳에 기록하세요.\n"
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        print(f"[{target_file}] 새로운 파일 및 템플릿 생성 완료!")
