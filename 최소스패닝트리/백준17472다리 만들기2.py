global n,m
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
visited={}
group={}
eltog={}
distance={}
rank={}
parent={}
dir=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(start):
    visited[start]=True
    group[start]=[start]
    q=[start]
    while q:
        x,y=q.pop(0)
        for i in dir:
            tx=x+i[0]
            ty=y+i[1]
            if tx>=0 and tx<=n-1 and ty>=0 and ty<=m-1:
                if (tx,ty) not in visited and l[tx][ty]==1:
                    visited[(tx,ty)]=True
                    q.append((tx,ty))
                    group[start].append((tx,ty))
def get_distance(start):
    sgroup=eltog[start]
    x,y=start
    for i in dir:
        tx=x
        ty=y
        count=-1
        while True:
            count+=1
            tx+=i[0]
            ty+=i[1]
            if tx<0 or tx>n-1 or ty<0 or ty>m-1:
                break
            if l[tx][ty]==1:
                comp=eltog[(tx,ty)]
                if sgroup==comp:
                    break
                else:
                    if (comp,sgroup) in distance:
                        break
                    elif (sgroup,comp) not in distance and count>=2:
                        distance[(sgroup,comp)]=count
                    elif (sgroup,comp) in distance and count>=2:
                        if count<distance[(sgroup,comp)]:
                            distance[(sgroup,comp)]=count
                    break
for i in range(n):
    for j in range(m):
        if l[i][j]==1 and (i,j) not in visited:
            bfs((i,j))
for i in group:
    temp=group[i]
    for j in temp:
        eltog[j]=i
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            get_distance((i,j))

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


def inintial(group):
    for vertex in group:
        parent[vertex] = vertex
        rank[vertex] = 0


def kruskal(group):
    edges=0
    summ=0
    a = list()
    l = [(i,distance[i]) for i in distance]
    l.sort(key=lambda x: x[1])
    inintial(group)
    for edge in l:
        if find(edge[0][0]) != find(edge[0][1]):
            union(edge[0][0], edge[0][1])
            summ+=edge[1]
            edges+=1
    if edges==len(group)-1:
        switch=True
    else:
        switch=False

    return summ , switch
a,b=kruskal(group)
if b==True:
    print(a)
else:
    print(-1)


