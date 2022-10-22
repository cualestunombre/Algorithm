def solution(gems):
    present = {}
    for i in gems:
        present[i]=True
    bucket = {}
    front,back=(0,0)
    answer=[0,0]
    value=100000000000000000
    bucket[gems[0]]=1
    while True:
        if len(bucket) == len(present):
            if value>back-front:
                answer[1]=back
                answer[0]=front
                value = back-front
            if front+1>=back:
                break
            bucket[gems[front]]-=1
            if bucket[gems[front]]==0:
                del bucket[gems[front]]
            front+=1
        else:
            if back+1>=len(gems):
                break
            back+=1
            if gems[back] not in bucket:
                bucket[gems[back]]=1
            else:
                bucket[gems[back]]+=1
    return [answer[0]+1,answer[1]+1]



