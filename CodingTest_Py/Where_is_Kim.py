def solution(seoul):
    location=0
    
    for someone in seoul:
        if(someone=='Kim'):        
            return '김서방은 {}에 있다'.format(location)
        location+=1
        
# format과 index 이용하면 숏코딩 가능
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))