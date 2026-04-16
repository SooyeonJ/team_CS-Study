import sys
arr = map(int,sys.stdin.read().split())
brr = []

for i in arr:
    remainder = i%42
    if remainder not in brr:
        brr.append(remainder)
    
print(len(brr))