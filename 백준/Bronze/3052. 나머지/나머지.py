import sys

arr = map(int, sys.stdin.read().split())
remainder = set()

for i in arr:
    remainder.add(i%42)
    
print(len(remainder))