def solution(cards1, cards2, goal):
    
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.remove(word)
        elif cards2 and cards2[0] == word:
            cards2.remove(word)
        else:
            return 'No'
    return 'Yes'
    
    
            