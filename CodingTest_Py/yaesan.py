def solution(d, budget):
    maxP=sum(d)
    if(maxP<=budget):
        return len(d)
    for i in d:
        maxP-=max(d)
        d.remove(max(d))
        if (maxP<=budget):
            return len(d)