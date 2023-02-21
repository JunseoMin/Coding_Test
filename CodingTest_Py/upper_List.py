#내 풀이
def solution(n):
    if(10>n): return [n]
    answer = []
    answer.append(n%10)
    return answer+solution(n//10)
#재귀함수를 이용한 풀이