#내 풀이
def solution(n):
    answer = 0
    while(n>=1):
        m=n%10
        n=n//10
        answer+=m
    return answer


#이상적 풀이
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 

#재귀함수 이용해서 자료구조로 해결 가능.