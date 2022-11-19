global n,m
import heapq as pq
road=[]
n,m = map(int,input().split())
adj={}
for i in range(m):
    a,b,t=map(int,input().split())
    if a in adj:
        adj[a].append((b,t))
    else:
        adj[a]=[(b,t)]
    if b in adj:
        adj[b].append((a,t))
    else:
        adj[b]=[(a,t)]
def dijkstra(start,end,x,y):
    q=[(0,start)]
    distance={start:0}
    check={}
    while q:
        time,node = pq.heappop(q)
        if distance[node]<time:
            continue
        for n,t in adj[node]:
            if (node==x and n==y) or (node==y and n==x):
                continue
            if n not in distance:
                if x==-1 and y==-1:
                    check[n]=node
                distance[n]=t+time
                pq.heappush(q,(distance[n],n))
            else:
                if distance[n]>time+t:
                    if x == -1 and y == -1:
                        check[n] = node
                    distance[n]=time+t
                    pq.heappush(q,(distance[n],n))
    if end in distance:
        if x==-1 and y==-1:
            cur = end
            while cur!=start:
                road.append((cur,check[cur]))
                cur=check[cur]
        return distance[end]
    else:
        return -1

time=dijkstra(1,n,-1,-1)
answer=0
for a,b in road:
    newTime = dijkstra(1, n, a, b)
    if newTime == -1:
        answer = -1
        break
    elif time < newTime and newTime - time > answer:
        answer = newTime - time
print(answer)






