import copy
def solution(sequence):
    a=copy.deepcopy(sequence)
    b=sequence
    for i in range(len(sequence)):
        if i%2==1:
            a[i]*=-1
        if i%2==0:
            b[i]*=-1
    maxVal=max(a[0],b[0])
    for i in range(1,len(a)):
        if a[i-1]>0 and a[i]+a[i-1]>0:
            a[i]+=a[i-1]
        if a[i]>maxVal:
            maxVal=a[i]
    for i in range(1,len(b)):
        if b[i-1]>0 and b[i]+b[i-1]>0:
            b[i]+=b[i-1]
        if b[i]>maxVal:
            maxVal=b[i]

    answer = maxVal
    return answer
