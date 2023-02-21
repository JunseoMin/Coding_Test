def ten_t_3(n):
    if(3>n): return [n%3]
    return ten_t_3(n//3)+[n%3]
#10진법을 입력받아 뒤집은 3진법으로 반환

def solution(n):
    ans=0
    j=0
    for i in ten_t_3(n):
        ans+=i*pow(3,j)
        j+=1
# j => 제곱수, ans=> 10진법
    return ans