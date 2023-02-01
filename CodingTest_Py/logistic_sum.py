import math
def solution(n):
    return (not(math.sqrt(n)%1>0) and math.pow(math.sqrt(n)+1,2)) or -1
#논리연산 활용 or는 앞의 연산이 참일경우 앞의 연산 결과값 반환