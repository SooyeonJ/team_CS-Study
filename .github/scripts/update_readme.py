import re, subprocess
from datetime import datetime, timedelta
t="| 날짜 | 요일 | SooyeonJ | Chobochoi | dori-2i |\n|:---:|:---:|:---:|:---:|:---:|\n"
us=['SooyeonJ','Chobochoi','dori-2i']
d={}
for u in us:
    rb=f"origin/{u}"
    try:
        fs=subprocess.check_output(['git','ls-tree','-r','--name-only',rb]).decode('utf-8').split('\n')
        for f in [x for x in fs if '백준/' in x or '프로그래머스/' in x]:
            if not re.search(r'\[(.*?)\] Title: (.*?),', f): continue
            try:
                log=subprocess.check_output(['git','log','-1','--format=%ad','--date=iso',rb,'--',f]).decode('utf-8').strip()
                if log:
                    dt=datetime.strptime(log[:19],"%Y-%m-%d %H:%M:%S")
                    if dt.hour==0: dt-=timedelta(days=1)
                    if dt.weekday() not in [0,2,4]: continue
                    ds=dt.strftime("%m-%d")
                    if ds not in d: d[ds]={x:0 for x in us}
                    d[ds][u]+=1
            except: pass
    except: pass
for k in sorted(d.keys(),reverse=True):
    wk=["월","화","수","목","금","토","일"][datetime.strptime(f"2026-{k}","%Y-%m-%d").weekday()]
    r=f"| {k} | {wk} |"
    for u in us: r+=f" O ({d[k][u]}) |" if d[k][u]>0 else " X |"
    t+=r+"\n"
with open('README.md','r',encoding='utf-8') as f: c=f.read()
with open('README.md','w',encoding='utf-8') as f:
    f.write(re.sub(r'.*?',f'\n{t}',c,flags=re.DOTALL))
