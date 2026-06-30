import os, subprocess
from datetime import datetime, timedelta

users = ['SooyeonJ', 'Chobochoi', 'dori-2i']
monthly_data = {}

# 깃허브 액션 환경의 타임존을 한국 표준시(KST)로 일치시킴
env = os.environ.copy()
env['TZ'] = 'Asia/Seoul'

def get_category(commit_hash):
    """커밋된 파일 확장자로 SQL/알고리즘을 명확히 구분"""
    try:
        files = subprocess.check_output(
            ['git', 'diff-tree', '--no-commit-id', '-r', '--name-only', commit_hash],
            stderr=subprocess.DEVNULL, env=env
        ).decode('utf-8').strip().split('\n')

        algo_extensions = ('.py', '.java', '.cpp', '.js', '.c', '.cs')

        for f in files:
            f_lower = f.lower()
            if f_lower.endswith('.sql'):
                return 'SQL'
            elif f_lower.endswith(algo_extensions):
                return '알고리즘'
                
    except subprocess.CalledProcessError:
        pass
    except Exception:
        pass
        
    return None

# 기존 코드의 for u in users: 내부 루프를 아래와 같이 수정하여 테스트

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
        print(f"[{u}] ❌ 브랜치 접근 실패: 해당 이름의 브랜치가 없거나 git log 에러 발생")
        continue

    for log in logs:
        if '|' not in log:
            continue
        parts = log.split('|', 2)
        if len(parts) < 3:
            continue
        commit_hash, dt_str, msg = parts

        if 'Title:' not in msg:
            print(f"  -> 제외됨 (사유: 'Title:' 없음) | 메시지: {msg[:20]}...")
            continue

        category = get_category(commit_hash)
        if not category:
            print(f"  -> 제외됨 (사유: 확장자 불일치 또는 분석 실패) | 커밋: {commit_hash[:7]}")
            continue
            
        print(f"  -> ✅ 유효 데이터 추가: {dt_str} | {category}")

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
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if s_mark in content and e_mark in content:
            before = content.split(s_mark)[0]
            after = content.split(e_mark)[-1]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(before + s_mark + table_content + e_mark + after)
    else:
        # 파일이 없을 경우 실행되는 기본 템플릿 생성 로직
        year_str, month_str = month_key.split('-')
        template_content = f"""# {year_str}년 {month_str}월 코딩테스트 현황

{s_mark}{table_content}{e_mark}
- 벌금 면제자 및 사유를 이곳에 기록하세요.
"""
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        print(f"새로운 마크다운 파일이 생성되었습니다: {target_file}")

# 파이썬 스크립트 내 해당 부분에 print 추가하여 테스트
    for log in logs:
        if '|' not in log:
            continue
        parts = log.split('|', 2)
        if len(parts) < 3:
            continue
        commit_hash, dt_str, msg = parts

        # 로그 확인용 (GitHub Actions 로그 탭에서 확인 가능)
        print(f"[{u}] 커밋 확인됨: {dt_str} / 메시지: {msg}")

        if 'Title:' not in msg:
            print(f" => 탈락: 'Title:' 문자열 없음")
            continue
