n = int(input())
r,d = map(int,input().split())
m = int(input())
l = [tuple(map(int,input().split())) for i in range(m)]
adj = {}
import heapq as pq
# h, t ,e1 ,e2
for h,t,e1,e2 in l:
    curh = h
    plus = 0
    while curh<=n:
        if e1+plus not in adj:
            adj[e1+plus] = [(e2+plus,t)]
        else:
            adj[e1+plus].append((e2+plus,t))
        if e2+plus not in adj:
            adj[e2+plus] = [(e1+plus,t)]
        else:
            adj[e2+plus].append((e1+plus,t))
        curh += 1
        plus += 1
visited = {}
q = [(0,r)]
while q:
    dist,node = pq.heappop(q)
    if node in visited and visited[node]<dist:
        continue
    if node not in adj:
        continue
    for nn,nd in adj[node]:
        if nn not in visited or visited[nn] > nd+dist:
            visited[nn] = nd+dist
            pq.heappush(q,(nd+dist,nn))

if d not in visited:
    print(-1)
else:
    print(visited[d])