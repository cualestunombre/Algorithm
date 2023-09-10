import heapq as pq
n,m,k = map(int,input().split())
adj = {}
for i in range(m):
    a,b,c = map(int,input().split())
    if a not in adj:
        adj[a] = [(b,c)]
    else:
        adj[a].append((b,c))

visited = {1:[0]}
for i in range(2,n+1):
    visited[i]=[]
q = [(0,1)]

checked = {}
checked[(1,0)] = True


while q:
    dist,node = pq.heappop(q)
    if len(visited[node]) == k and -visited[node][0] < dist: #전파 x
        continue

    if node not in adj:
        continue
    for nn,nd in adj[node]:
        if len(visited[nn]) < k:
            pq.heappush(q,(dist+nd,nn))
            pq.heappush(visited[nn],-(dist+nd))

        elif len(visited[nn]) == k and nd+dist < -visited[nn][0]:
            pq.heappush(visited[nn],-(dist+nd))
            pq.heappop(visited[nn])
            pq.heappush(q,(dist+nd,nn))
for i in range(1,n+1):
    if i not in visited or len(visited[i])!= k:
        print(-1)
    else:
        print(-visited[i][0])