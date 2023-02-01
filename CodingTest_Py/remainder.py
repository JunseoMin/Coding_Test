def solution(n):
    if(n%2==1):  return 2
    for m in range(3,n,2):
        if((n-1)%m==0):
            return m

# 짝수/ 홀수 나누어서 멤모리 최적화, 홀수의 가장 작은 인수 구하기