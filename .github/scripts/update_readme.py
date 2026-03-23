import os
import re

table = "| 플랫폼 | 레벨 | 문제 제목 |\n|---|---|---|\n"
platforms = ['백준', '프로그래머스']

for p in platforms:
    if not os.path.isdir(p):
        continue
    for lvl in os.listdir(p):
        lvl_path = os.path.join(p, lvl)
        if not os.path.isdir(lvl_path):
            continue
        for folder in os.listdir(lvl_path):
            match = re.search(r'\[(.*?)\] Title: (.*?),', folder)
            if match:
                level = match.group(1)
                title = match.group(2)
                table += f"| {p} | {level} | {title} |\n"

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(
    r'.*?',
    f'\n{table}\n',
    content,
    flags=re.DOTALL
)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
