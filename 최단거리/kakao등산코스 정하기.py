import heapq
import copy
def solution(n, paths, gates, summits):
    gate={}
    nchecked={}
    summit={}
    adj={}
    intensity = {}
    for _ in gates:
        gate[_]=True
        nchecked[_]=True
    for _ in summits:
        summit[_]=True
    for i,j,k in paths:
        if i not in adj:
            adj[i]=[(j,k)]
        else:
            adj[i]+=[(j,k)]
        if j not in adj:
            adj[j]=[(i,k)]
        else:
            adj[j]+=[(i,k)]
    nlist = copy.deepcopy(gates)
    while nlist:
        del nchecked[nlist[0]]
        start=nlist[0]
        intensity[start]=0
        q=[(0,start)]
        while q:
            x,y = heapq.heappop(q) # x:intensity y:node
            if intensity[y]<x:
                continue
            for a,b in adj[y]: # a: node b: time
                if a in summit:
                    if a in intensity:
                        if max(x,b)<intensity[a]:
                            intensity[a]=max(x,b)
                    else:
                        intensity[a]=max(x,b)
                elif a in gate:
                    if a not in intensity:
                        del nchecked[a]
                        intensity[a]=0
                        heapq.heappush(q,(0,a))
                else:
                    if a not in intensity:
                        intensity[a]=max(x,b)
                        heapq.heappush(q,(max(x,b),a))
                    else:
                        if max(x,b)<intensity[a]:
                            intensity[a]=max(x,b)
                            heapq.heappush(q,(max(x,b),a))
        nlist=list(nchecked.keys())
    answer=[]
    for _ in summits:
        if _ in intensity:
            answer.append([_,intensity[_]])
    answer.sort(key=lambda x:(x[1],x[0]))
    return answer[0]
solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1,3],[5])