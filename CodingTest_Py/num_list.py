def solution(arr, divisor):
    for n in arr:
        print(n%divisor)
        if(n%divisor):
            arr.remove(n)
    return arr or [-1]
# for 문으로 배열 접근시 index가 기준임


S=solution([5, 9, 7, 10],5)
print(S)