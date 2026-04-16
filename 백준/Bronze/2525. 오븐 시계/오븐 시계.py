h,m=map(int,input().split())
t=int(input())
t1 = m+t

if h+(t1//60)>23:
    print((h+(t1//60))-24,t1%60)
else:
    print((h+(t1//60)),t1%60)