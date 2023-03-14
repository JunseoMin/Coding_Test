def solution(s, n):
    k=''
    for m in s:
        if(m==' '):
            k+=' '
        elif(m.islower()):
            if(ord(m)+n>ord('z')):
                k+=chr(ord(m)+n-26)
            else: k+=chr(ord(m)+n)
        else:
            if(ord(m)+n>ord('Z')):
                k+=chr(ord(m)+n-26)
            else: k+=chr(ord(m)+n)
    
    return k

#26뺐는데 왜됨? 알파벳이 26개니까 ㅋ