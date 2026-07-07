def solution(strings, n):
    answer = []
    print([strings[i][n] for i in range(len(strings))])
    print(strings.sort(key=lambda x:[strings[i][n] for i in range(len(strings))]))
    return answer