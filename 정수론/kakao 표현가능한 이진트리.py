def toBinary(n):
    temp=""
    comp=0
    while True:
        if 2**comp>n:
            comp-=1
            break
        else:
            comp+=1
    while comp>=0:
        if n-2**comp>=0:
            temp=temp+"1"
            n-=2**comp
        else:
            temp=temp+"0"
        comp-=1
    return temp
def target(n):
    length = len(n)
    if length == 1 or length == 3 or length == 7 or length == 15 or length == 31 or length ==63:
        return n
    elif length==2:
        return "0"+n
    elif length>3 and length<7:
        return "".join(["0" for i in range(7-length)])+n
    elif length>7 and length<15:
        return "".join(["0" for i in range(15-length)])+n
    elif length>15 and length<31:
        return "".join(["0" for i in range(31-length)])+n
    elif length > 31 and length < 63:
        return "".join(["0" for i in range(63-length)])+n
def isLegit(n):
    length=len(n)
    m=length//2
    if length==1:
        return True
    target = n[(length-1)//2]
    if target=='1':
        if isLegit(n[:length//2]) and isLegit(n[length//2+1:]):
            return True
    else:
        if isLegit(n[:length // 2]) and isLegit(n[length // 2 + 1:]) and n[(m-1)//2]=='0' and n[(m+length)//2]=='0':
            return True



def solution(numbers):
    answer=[]
    for i in numbers:
        binary=target(toBinary(i))
        if isLegit(binary):
            answer.append(1)
        else:
            answer.append(0)
    return answer
print(solution([63, 111, 95]))
