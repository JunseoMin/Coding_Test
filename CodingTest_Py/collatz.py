def solution(n,res=0):
    if(n==1):   return res 
    if(res==500):   return -1

    if(n%2):
        return solution(n*3+1,res+1)
    else:   
        return solution(n/1,res+1)
    
    # 리컬전이용하여 구현 변수 default이용하여 함수 하나로 리턴함   