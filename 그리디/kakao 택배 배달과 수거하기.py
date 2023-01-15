def solution(cap, n, deliveries, pickups):
    dstack=[]
    pstack=[]
    dist=0
    for i in range(len(deliveries)):
        if deliveries[i]!=0:
            dstack.append([deliveries[i],i+1]) #개수,거리
        if pickups[i]!=0:
            pstack.append([pickups[i],i+1])
    while pstack or dstack:
        cur=cap
        curs=cap
        if pstack and dstack:
            target=max(pstack[-1][1],dstack[-1][1])
        elif pstack and not dstack:
            target=pstack[-1][1]
        elif not pstack and dstack:
            target=dstack[-1][1]
        dist+=target*2
        while dstack:
            if dstack[-1][0]<=cur:
                cur-=dstack.pop()[0]
            else:
                dstack[-1][0]-=cur
                break
        while pstack:
            if pstack[-1][0]<=curs:
                curs-=pstack.pop()[0]
            else:
                pstack[-1][0]-=curs
                break
    return dist