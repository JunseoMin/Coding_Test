def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings

#lambda 함수를 이용해서 sort할때 인자로 선택할 key값 지정 가능