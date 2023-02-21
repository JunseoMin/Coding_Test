#my solution
def solution(s):
    ans=[]
    s=s.upper()
    slist=s.split(" ")
    for ss in slist:
        i=0
        anss=''
        for l in ss:
            if(i%2):
                anss+=l.lower()
            else: anss+=l
            i+=1
        ans.append(anss)
    return ' '.join(ans)


#to be
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# enumerate 함수를 이용하면 index애 바로 접근이 가능.
map(lambda 변수: 실행할함수 , 변수를어디서가저올지)