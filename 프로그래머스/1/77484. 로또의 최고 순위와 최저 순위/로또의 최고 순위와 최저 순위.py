def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    
    match_count=0
    
    for x in lottos:
        if x in win_nums:
            match_count+=1
            
    max_match = match_count+zero_count
    min_match = match_count
    
    return [min(6,7-max_match),min(6,7-min_match)]