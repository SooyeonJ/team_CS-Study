def solution(n):
    answer=[]
    d=2
    temp = n
    while d*d<=temp:
        if temp%d==0:
            answer.append(d)
            while temp%d==0:
                temp//=d
        d+=1
        
    if temp>1:
        answer.append(temp)
        
    return answer    