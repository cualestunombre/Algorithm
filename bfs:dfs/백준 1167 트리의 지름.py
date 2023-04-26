n=int(input())
dist={}
def dfs(start):
    stack=[(start,0)]
    distance={start:0}
    while stack:
        node,value = stack.pop()
        for x,y in dist[node]:
            if x not in distance:
                distance[x]=value+y
                stack.append((x,y+value))

    n,maxx=(0,0)
    for i in distance:
        if distance[i]>maxx:
            maxx=distance[i]
            n = i
    return maxx, n

for i in range(n):
    l=list(map(int,input().split()))
    number = l.pop(0)
    l.pop()
    dist[number]=[]
    while l:
        # i+1과 a의 거리가 b
        b=l.pop()
        a=l.pop()
        dist[number].append((a,b))

value,node = dfs(1)
value,node = dfs(node)
print(value)