def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def doSegmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4):

    orient1 = ccw(x1, y1, x2, y2, x3, y3)
    orient2 = ccw(x1, y1, x2, y2, x4, y4)
    orient3 = ccw(x3, y3, x4, y4, x1, y1)
    orient4 = ccw(x3, y3, x4, y4, x2, y2)


    if (orient1 * orient2 < 0) and (orient3 * orient4 < 0):
        return True


    if (orient1 == 0 and isPointOnSegment(x1, y1, x2, y2, x3, y3)):
        return True
    if (orient2 == 0 and isPointOnSegment(x1, y1, x2, y2, x4, y4)):
        return True
    if (orient3 == 0 and isPointOnSegment(x3, y3, x4, y4, x1, y1)):
        return True
    if (orient4 == 0 and isPointOnSegment(x3, y3, x4, y4, x2, y2)):
        return True

    return False

def isPointOnSegment(x1, y1, x2, y2, x, y):
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)
group, parent,pos,cur = {},{},{},{}

def union(u,v):
    parentU,parentV = find(u),find(v)
    groupU,groupV = group[parentU],group[parentV]

    if parentU == parentV:
        return
    if groupU >= groupV:
        parent[parentV] = parentU
        group[parentU] += groupV
    else:
        parent[parentU] = parentV
        group[parentV] += groupU


def find(u):
    if parent[u] == u:
        return u
    ret = find(parent[u])
    parent[u] = ret
    return ret



n = int(input())
for i in range(n):
    parent[i],group[i] = i,1
    pos[i]=tuple(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        a,b,c,d = pos[i]
        e,f,g,h = pos[j]
        #선분이 교차한다면
        if doSegmentsIntersect(a,b,c,d,e,f,g,h):
            union(i,j)

unique = set()
ans = []
for i in pos:
    unique.add(find(i))
    ans.append(group[find(i)])
ans.sort(reverse=True)
print(len(unique))
print(ans[0])


