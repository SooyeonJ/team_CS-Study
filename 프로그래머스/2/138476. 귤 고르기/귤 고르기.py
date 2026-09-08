def solution(k, tangerine):
    dic={}
    count=0
    for x in tangerine:
        dic[x]=dic.get(x,0)+1
    
    for i,y in enumerate(sorted(dic.values(),reverse=True)):
        count+=y
        if count>=k:
            return i+1
            