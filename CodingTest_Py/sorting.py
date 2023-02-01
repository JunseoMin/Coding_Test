def numlist(n):
    if(n<10):   return n
    numl=[n%10]
    return numl+numlist(n//10)

def solution(n):
    Nlist=numlist(n)
    res=Nlist.sort(reverse=True)
    print(res)
    
    return res