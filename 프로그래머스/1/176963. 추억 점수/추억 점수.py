def solution(name, yearning, photo):
    result=[]
    dict={}
    for nm,year in zip(name,yearning):
        dict[nm]=year
    
    for h in photo:
        sol=0
        for y in h:
            sol+=dict.get(y,0)
        result.append(sol)
    return result
            