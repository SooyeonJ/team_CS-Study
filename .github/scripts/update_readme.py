import re, subprocess
from datetime import datetime

t = "| 요일 | 작성자 | 플랫폼 | 레벨 | 문제 |\n|---|---|---|---|---|\n"
br_out = subprocess.check_output(['git', 'branch', '-r']).decode('utf-8')
brs = [b.strip() for b in br_out.split('\n') if b.strip() and '->' not in b and 'main' not in b]

for b in brs:
    try:
        fs_out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', b]).decode('utf-8')
        fs = [f for f in fs_out.split('\n') if f.startswith('백준/') or f.startswith('프로그래머스/')]
    except: continue
    for f in fs:
        m = re.search(r'\[(.*?)\] Title: (.*?),', f)
        if m:
            try:
                log = subprocess.check_output(['git', 'log', '-1', '--format=%aN|%aD', b, '--', f]).decode('utf-8').strip()
                if not log: continue
                a, dt_str = log.split('|')
                dt = datetime.strptime(dt_str, "%a, %d %b %Y %H:%M:%S %z")
                day = ["월", "화", "수", "목", "금", "토", "일"][dt.weekday()]
            except: day, a = "-", "-"
            p = '백준' if f.startswith('백준') else '프로그래머스'
            t += f"| {day} | {a} | {p} | {m.group(1)} | {m.group(2)} |\n"

with open('README.md', 'r', encoding='utf-8') as f: c = f.read()
nc = re.sub(r'.*?', f'\n{t}\n', c, flags=re.DOTALL)
with open('README.md', 'w', encoding='utf-8') as f: f.write(nc)
