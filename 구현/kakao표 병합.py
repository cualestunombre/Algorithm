def union(u, v,mode):
    root1 = find(u)
    root2 = find(v)
    if mode==0:
        parent[root2] = root1
    else:
        parent[root1] = root2
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]
def inintial():
    for i in range(1,51):
        for j in range(1,51):
            parent[(str(i),str(j))]=(str(i),str(j))
values={}#그룹의 값 정보
parent={} #그룹의 부모 정보
grouped={} #그룹화 정보
def handleUpdate(temp):
    if len(temp)==4:
        values[find((temp[1],temp[2]))]=temp[3]
    else:
        op, val1,val2 = temp
        for i in values:
            if values[i]==val1:
                values[i]=val2

def handleMerge(temp):
    op,r1,c1,r2,c2 = temp
    if (r1,c1) == (r2,c2):
        return
    grouped[(r1,c1)]=True
    grouped[(r2,c2)]=True
    if find((r1,c1)) in values and find((r2,c2)) in values:
        if find((r1,c1))==find((r2,c2)):
            return
        del values[find((r2,c2))]
        union((r1,c1),(r2,c2),0)
    elif find((r1,c1)) in values and find((r2,c2)) not in values:
        union((r1,c1),(r2,c2),0)
    elif find((r1,c1)) not in values and find((r2,c2)) in values:
        union((r1,c1),(r2,c2),1)
    else:
        union((r1,c1),(r2,c2),0)

def handleUnmerge(temp):
    toDel=[]
    op,r,c=temp
    value=""
    if find((r,c)) in values:
        value=values[find((r,c))]
    com=find((r,c)) #root노드
    for x,y in grouped:
        if find((x,y))==com:
            toDel.append((x,y))
    for i in toDel:
        parent[i]=i
        del grouped[i]
        if i in values:
            del values[i]
    if (value)!='':
        values[(r,c)]=value


def handlePrint(temp):
    op,r,c = temp
    if find((r,c)) in values:
        return values[find((r,c))]
    else:
        return 'EMPTY'

def solution(commands):
    answer = []
    inintial()
    for i in commands:
        temp = i.split()
        if temp[0]=='UPDATE':
            handleUpdate(temp)
        elif temp[0]=='MERGE':
            handleMerge(temp)
        elif temp[0]=='UNMERGE':
            handleUnmerge(temp)
        else:
            answer.append(handlePrint(temp))
    return answer
a=solution(["PRINT 1 2","UNMERGE 1 1",'MERGE 1 1 1 2','MERGE 1 2 1 1','UPDATE 1 1 ho','PRINT 1 2','MERGE 1 2 1 1','PRINT 1 1'])
print(a)
print(values)
