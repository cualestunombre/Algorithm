def bfs(option,n,k): #option은 최소비용
    if opition==-1:
        q=[1]
        visited={1:0}
        while q:
            node = q.pop(0)
            for x in dic[node]:
                if x not in visited:
                    visited[x]=visited[node]+1
                    q.append(x)
        if n in visited:
            return visited[n]
        else:
            return False






n,p,k = map(int,input().split())
dic={}
for i in range(p):
    x,y,z=map(int,input().split())
    if x in dic:
        dic[x]+=[(y,z)]
    else:
        dic[x]=[(y,z)]
    if y in dic:
        dic[y]+=[(x,z)]
    else:
        dic[y]=[(x,z)]
switch=bfs(-1,n,k)
if not switch:
    print(-1)
elif switch<=k:
    print(0)
else:
    start=0
    end=1000000
    ans=0
    while start<end:
        mid=(start+end)//2
        if bfs(mid,n,k)==True:
            start=mid+1
            ans=mid
        else:
            end=mid-1
    print(ans)





