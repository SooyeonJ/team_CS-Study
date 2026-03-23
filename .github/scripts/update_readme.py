import re, subprocess

t = "| 월 | 팀원 | 플랫폼 | 레벨 | 문제 |\n|---|---|---|---|---|\n"
targets = ['SooyeonJ', 'Chobochoi', 'dori-2i']
d = []

for b in targets:
    remote_b = f"origin/{b}"
    try:
        # 지정된 원격 브랜치의 파일 목록 추출
        fs_out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', remote_b]).decode('utf-8')
        fs = [x for x in fs_out.split('\n') if x.startswith('백준/') or x.startswith('프로그래머스/')]
    except subprocess.CalledProcessError:
        continue

    for f in fs:
        m = re.search(r'\[(.*?)\] Title: (.*?),', f)
        if m:
            try:
                # 파일이 생성/수정된 날짜만 추출
                log = subprocess.check_output(['git', 'log', '-1', '--format=%ad', '--date=short', remote_b, '--', f]).decode('utf-8').strip()
                if log:
                    month = log[:7] # YYYY-MM 형식 지정
                    platform = '백준' if f.startswith('백준') else '프그'
                    d.append((month, b, platform, m.group(1), m.group(2)))
            except subprocess.CalledProcessError:
                pass

# 월(내림차순) -> 팀원 이름 순으로 정렬
d.sort(key=lambda x: (x[0], x[1]), reverse=True)

for x in d:
    t += f"| {x[0]} | {x[1]} | {x[2]} | {x[3]} | {x[4]} |\n"

# README.md 파일 읽기 및 쓰기
with open('README.md', 'r', encoding='utf-8') as file:
    c = file.read()

new_c = re.sub(
    r'.*?', 
    f'\n{t}', 
    c, 
    flags=re.DOTALL
)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(new_c)
