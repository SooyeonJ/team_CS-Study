#260325
def solution(s):
    st = []
    
    for char in s:
        if char == '(':
            st.append(char)
        elif char == ')':
            if len(st) != 0:
                st.pop()
            else:
                return False
            
    return len(st) == 0
            
        
        
        