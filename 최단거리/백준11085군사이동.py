import heapq as pq
def dijkstra(adj,c,v):
    dist={}
    q=[(0,c)]
    dist[c]=100000000
    while q:
        cost,node = pq.heappop(q)
        for nnode,cost in adj[node]:
            if nnode not in dist:
                dist[nnode]=min(cost,dist[node])
                pq.heappush(q,(dist[nnode],nnode))
            else:
                if min(cost,dist[node])>dist[nnode]:
                    dist[nnode]=min(cost,dist[node])
                    pq.heappush(q,(dist[nnode],nnode))
    return dist[v]

p,w = map(int,input().split())
c,v = map(int,input().split())
adj={}
for i in range(w):
    x,y,z=map(int,input().split())
    if x not in adj:
        adj[x]=[(y,z)]
    else:
        adj[x].append((y,z))
    if y not in adj:
        adj[y]=[(x,z)]
    else:
        adj[y].append((x,z))
print(dijkstra(adj,c,v))