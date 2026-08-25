def solution(n, m, section):
    sol = [1]*(n+1)
    
    for x in section:
        sol[x]=0
    
    print(sol)
    