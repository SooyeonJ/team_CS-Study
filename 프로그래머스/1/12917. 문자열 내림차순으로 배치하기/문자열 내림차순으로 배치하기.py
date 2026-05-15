def solution(s):
    
    return ''.join(sorted([x for x in s if x==x.lower()],reverse=True)+sorted([x for x in s if x==x.upper()],reverse=True))
                                                                     