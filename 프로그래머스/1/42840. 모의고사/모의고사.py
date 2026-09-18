def solution(answers):
    gum1=[1,2,3,4,5]*len(answers)
    gum2=[2,1,2,3,2,4,2,5]*len(answers)
    gum3=[3,3,1,1,2,2,4,4,5,5]*len(answers)
    result =[0,0,0]
    for i in range(len(answers)):
        if answers[i]==gum1[i]:
            result[0]+=1
        if answers[i]==gum2[i]:
            result[1]+=1
        if answers[i]==gum3[i]:
            result[2]+=1
    l=max(result)
    conclusion=[]
    for i in range(len(result)):
        if result[i]==l:
              conclusion.append(i+1)
                   
    return conclusion