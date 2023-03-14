def solution(left, right):
    if(left>right):
        return 0
    
    if(pow(left,0.5)%1):
        return solution(left+1,right)+left
    else:
        return solution(left+1,right)-left
    
print(solution(20,70))