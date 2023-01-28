db={}
def calculateMax(lists):
    temp={}
    for i in range(len(lists)):
        temp[i]=lists[i][-1][1]
    for i in range(len(lists)-1,-1,-1):
        if i ==len(lists)-1:
            db[i]=temp[i]
        else:
            if db[i+1]<temp[i]:
                db[i]=temp[i]
            else:
                db[i]=db[i+1]
def solution(scores):
    rank={}
    total = scores[0][0]+scores[0][1]
    mx,my = scores[0]
    scores.sort(key=lambda x:(x[0],x[1]))
    lists=[]
    cand=[]
    for x,y in scores:
        if not lists:
            lists.append([(x,y)])
        elif lists[-1][-1][0]==x:
            lists[-1].append((x,y))
        else:
            lists.append([(x,y)])
    calculateMax(lists)
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if i!=len(lists)-1:
                if lists[i][j][1]>=db[i+1]:
                    cand.append(lists[i][j])
            else:
                cand.append(lists[i][j])
    cand.sort(key=lambda x:(-(x[0]+x[1])))
    q=[]
    for x,y in cand:
        if not q:
            q.append([x+y])
        elif q[-1][-1]!=x+y:
            q.append([x+y])
        else:
            q[-1].append(x+y)
    cr = 1
    for i in range(len(q)):
        rank[q[i][0]]=cr
        cr+=len(q[i])

    if (mx,my) not in cand:
        return -1
    return rank[total]
