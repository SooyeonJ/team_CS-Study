def solution(s):
    token = []
    dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
            'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for i, val in enumerate(s):
        if val.isdigit() == True:
            token.append(val)
        else:
            for word in dict.keys():
                if s[i:].startswith(word):
                    token.append(str(dict.get(word)))
    return int(''.join(token))