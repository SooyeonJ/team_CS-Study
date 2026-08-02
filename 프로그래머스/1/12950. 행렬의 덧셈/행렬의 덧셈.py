def solution(arr1, arr2):
    

    '2중 중첩 리스트 컴프리핸션'
    '바깥쪽 zip(arr1,arr2) : 행 단위로 짝 지어준다.'
    '1번째 바퀴에서 넘어온 r1=[1,2]와 r2=[3,4]를 가지고 안쪽 zip을 돌린다. 안쪽 zip은 숫자(원소) 단위로 짝지어준다.'
    return [[c1+c2 for c1,c2 in zip(r1,r2)] for r1,r2 in zip(arr1,arr2)]
    
        