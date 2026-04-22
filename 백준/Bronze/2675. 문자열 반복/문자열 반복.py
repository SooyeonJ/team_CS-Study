T=int(input())
data = [input().split() for _ in range(T)]

for r_str, s_str in data:
    R=int(r_str)
    for i in s_str:
        print(i*R, end='')
    print()