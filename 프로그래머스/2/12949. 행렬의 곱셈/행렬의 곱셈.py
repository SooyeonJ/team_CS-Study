def solution(arr1, arr2):
    
    'append문이 아니라 +=문을 쓰려면 미리 초기화가 필요'
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    '행렬 곱셈 AXB=C가 성립하려면 A의 열 개수와 B의 행 개수가 반드시 같아야한다.'
    'arr1의 크기 : Mxk arr2의 크기 : kxN'
    '결과 행렬 answer의 크기 : MxN'
    '3중 for 문으로 계산하기'
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j]+=arr1[i][k] * arr2[k][j]
                
    
    return answer
            

            
    