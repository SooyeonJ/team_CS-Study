def solution(number):
    
    sorted(number)
    
    count=0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for z in range(j+1,len(number)):
                if number[i]+number[j]+number[z]==0:
                    count+=1
    if count!=0:
        return count
    else:
        return 0
    
    