# 내 풀이
def solution(n):
    answer = 0
    i=1
    if(n==0):   return 0
    if(n==1):   return 1
    while i!=n:
        if(n%i==0):
            answer+=i
        i+=1
    answer+=n

    return answer

#이상적 풀이법
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# range로 범위 지정하면 계산하기 편리함
# 2로 나눈 나머지 이용해서 성능 최적화 가능함.

#sum 함수 생각하기.
