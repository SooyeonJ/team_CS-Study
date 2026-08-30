def solution(s):
    'replace() 함수는 문자열(str)끼리만 치환할 수 있다.'
    character={'zero':'0','one':'1','two':
               '2','three':'3','four':'4',
              'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for word,num in character.items():
        s=s.replace(word,num)
        
    return int(s)
                
            
        
    
    