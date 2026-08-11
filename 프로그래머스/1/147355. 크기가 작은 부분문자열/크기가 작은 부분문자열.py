def solution(t, p):
    l=len(p)
    i=0
    sol=[]
    while l<=len(t):
        sol.append(t[i:l:])
        i+=1
        l+=1
    result=0
    for x in sol:
        if x<=p:
            result+=1
    
    return result
        