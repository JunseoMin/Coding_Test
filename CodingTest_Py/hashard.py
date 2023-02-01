def sumnum(n):
    if(10>n):   return n
    return (n%10)+sumnum(n//10)

def solution(x):
    return (x%sumnum(x))==0