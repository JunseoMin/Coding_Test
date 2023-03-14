def solution_wrong(d, budget):
    maxP=sum(d)
    if(maxP<=budget):
        return len(d)
    for i in d:
        maxP-=max(d)
        d.remove(max(d))
        if (maxP<=budget):
            return len(d)
        

solution_wrong(	[9,9,11],6)


        
def solution_correct(d, budget):
    maxP=sum(d)
    if(maxP<=budget):
        return len(d)
    #시간 최소화
    for i in range(len(d)):
        maxP-=max(d)
        d.remove(max(d))
        if (maxP<=budget):
            return len(d)
        
        
# 결국 리턴값이 배열의 크기 반환이므로 가장 큰 값을 차지하는 요청금액을 배열에서 삭제하고, 그 총 합값이 budget보다 작으면 리턴후 함수 종료하려함 테스트 통과 못하는 이유 모르겠음
# for 문의 반복 iterator를 배열 d로 할 경우에는 컴파일이 안되는데 그 이유는...?