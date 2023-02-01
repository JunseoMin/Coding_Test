def solution(s):
    return  ''.join(sorted(s,reverse=True))
# join 함수는 문자열 list합치기 가능하게 해줌
# sorted 함수에서 reverse=True 인자 넣을 수 있음