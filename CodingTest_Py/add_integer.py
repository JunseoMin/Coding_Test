def solution(a, b):
    return ((a==b) and a) or (sum(range(a,b+1)) or sum(range(b,a+1)))