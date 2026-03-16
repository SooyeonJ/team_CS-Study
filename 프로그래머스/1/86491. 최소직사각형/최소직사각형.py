def solution(sizes):
    h=0
    w=0
    
    for tag in sizes:
        hmin = min(tag)
        wmax = max(tag)
        if hmin>h:
            h=hmin
        if wmax>w:
            w=wmax
    return h*w
            