def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

#python에서 문자열이 있으면 true로 판단, int 0/1모두 boolean 값으로 판별 가능
#앞의 논리연산부터 계산한다.