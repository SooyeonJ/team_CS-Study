def solution(s):
    
    if len(s)==4 or len(s)==6:
        result = True if s.isdigit() else False
        return result
    
    return False

        