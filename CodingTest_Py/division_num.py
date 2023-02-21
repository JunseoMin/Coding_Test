def solution(arr, divisor):
    ret=[]
    for e in arr:
        if(not e%divisor):
            ret.append(e)
    ret.sort()
    return ret if ret else [-1]

# []안 list값 range로 넣는법 숙지하기
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]