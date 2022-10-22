n=int(input())
answer=0
l=[tuple(map(int,input().split()))]
l.sort(key=lambda x:(-x[1]))
visited = {}
for i in l:
    day=i[1]
    while day>0:
        if day in visited:
            day-=1
    if day==0:
        pass
    else:
        visited[day]=True
        answer+=i[0]
print(visited)
print(answer)
