data = input().upper()
counts={}

for char in data:
    if char in counts:
        counts[char]+=1
    else:
        counts[char]=1
        
max_val=max(counts.values())
max_data=[]

for char in counts:
    if counts[char]==max_val:
        max_data.append(char)
        
if len(max_data)>1:
    print('?')
else:
    print(max_data[0])