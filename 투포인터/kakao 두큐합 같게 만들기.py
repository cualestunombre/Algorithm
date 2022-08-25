def solution(queue1, queue2):
    l = queue1 + queue2
    target= 0
    for i in queue1:
        target+=i
    for j in queue2:
        target+=j
    if target%2!=0:
        answer=-1
    else:
        got = 0
        cnt=0
        target = target // 2
        for i in queue1:
            got+=i
        forward =0
        back=len(queue1)-1
        switch=False
        while True:

            if got>target:
                forward+=1
                cnt+=1
                if forward>back:
                    break
                got-=l[forward-1]
            elif got==target:
                switch=True
                break
            elif got<target:
                back+=1
                cnt+=1
                if back>len(queue1)*2-1:
                    break
                got+=l[back]
        if switch==True:
            answer = cnt
        else:
            answer=-1

    return answer



solution([3, 2, 7, 2],[4, 6, 5, 1])