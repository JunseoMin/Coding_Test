def solution(numbers):
    answer=[]
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if(i!=j):
                if(not((numbers[i]+numbers[j]) in answer)):
                    answer.append(numbers[i]+numbers[j])
    set(answer)
    answer.sort()
    return answer

## set함수를 이용하면 중복문자 삭제가능