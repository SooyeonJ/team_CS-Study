def solution(sizes):
    x=[]
    y=[]
    for h,w in sizes:
        if(w>=h):
            x.append(w)
            y.append(h)
        elif h>w:
            x.append(h)
            y.append(w)
            
    return max(x)*max(y)
            