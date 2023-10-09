rank,parent,path,seq,cons = {},{},{},[],{}
n,m,q = map(int,input().split())


def find(u):
    if parent[u] == u:
        return u
    else:
        parent[u] = find(parent[u])
        return parent[u]

def union(u,v):
    #부모가 같으면 병합할 필요가 없음
    parentU,parentV  = find(u),find(v)
    if parentU == parentV:
        return 0

    if rank[parentU] >= rank[parentV]:
        ret = rank[parentU]*rank[parentV]
        parent[parentV] = parentU
        rank[parentU] += rank[parentV]
        return ret

    else:
        ret = rank[parentU]*rank[parentV]
        parent[parentU] = parentV
        rank[parentV] += rank[parentU]
        return ret

#초기화
for i in range(1,n+1):
    parent[i] = i
    rank[i] = 1

for index in range(m):
    a,b = map(int,input().split())
    path[index+1] = (a,b)
for index in range(q):
    number = int(input())
    seq.append(number)
    cons[number] = True

for i in path:
    if i not in cons:
        a,b = path[i]
        union(a,b)
total = 0
seq.reverse()
for i in seq:
    u,v = path[i]
    total += union(u,v)
print(total)

