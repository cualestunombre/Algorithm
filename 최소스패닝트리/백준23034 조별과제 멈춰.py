from collections import deque
v, e = map(int, input().split())
info = list()
for i in range(e):
    info.append(list(map(int, input().split())))
q=int(input())
query=[list(map(int,input().split())) for i in range(q)]

graph = {'vertices': [],
         'edges': []}
for i in range(v):
    graph['vertices'] += [i + 1]
for i in range(e):
    graph['edges'] += [[info[i][2], info[i][0], info[i][1]]]
rank = dict()
parent = dict()
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if root1 == root2:
            rank[root1] += 1
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]
def inintial(graph):
    for vertex in graph['vertices']:
        parent[vertex] = vertex
        rank[vertex] = 0
def kruskal(graph):
    a = list()
    l = graph['edges']
    l.sort(key=lambda x: x[0])
    inintial(graph)
    for edge in l:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            a.append(edge)
    return a
    # 초기화 하고
    # 유니온 하고
    # 파인드 한다
l = kruskal(graph)
expense=0
for i in l:
    expense+=i[0]
adj={}
for a,b,c in l:
    if b in adj:
        adj[b].append((c,a))
    else:
        adj[b]=[(c,a)] #노드,비용
    if c in adj:
        adj[c].append((b,a))
    else:
        adj[c]=[(b,a)]
answer=[]
for x,y in query:
    q=deque()
    q.append(x)
    visited={x:True}
    while q:
        node = q.popleft()
        for v,e in adj[node]:
            if v not in visited:
                visited[v]=(node,e)
                q.append(v)
    maxx=0
    current=y
    while current!=x:
        if visited[current][1]>maxx:
            maxx=visited[current][1]
        current=visited[current][0]
    answer.append(expense-maxx)
for i in answer:
    print(i)




