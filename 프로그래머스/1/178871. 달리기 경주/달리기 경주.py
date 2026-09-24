def solution(players, callings):
    '해시함수니깐 딕셔너리 이용하기 value 값은 등수-1'
    player_index = {player : i for i,player in enumerate(players)}
    
    '계산해야 하는 값 바로 앞의 선수, 이름 불린 선수 swap'
    for call in callings:
        'call 풀린 선수 index가 몇번째인지 알아내야 함'
        call_player = player_index[call]
        'call 불린 선수 앞의 선수가 누구인지 알아내야함'
        front_player = players[call_player-1]
        'players에서 자리 swap 필요'
        players[call_player],players[call_player-1] = players[call_player-1], players[call_player]
        'player_index 수 증/감 필요, 이름이 여러번 불리기 때문에 index 숫자 변화 필요'
        player_index[call]=call_player-1
        player_index[front_player]=call_player
        
        
        
    return players
        
        
            
    
                