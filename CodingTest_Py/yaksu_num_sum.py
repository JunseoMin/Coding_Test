import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
#파이썬 최대 리컬젼 해제

def solution(left, right):   
    if(left>right):
        return 0 
    if(pow(left,0.5)%1):
        return solution(left+1,right)+left
    else:
        return solution(left+1,right)-left
    