n = int(input())
l=[list(map(int,input().split()))for i in range(n)]
l.sort( key=lambda x:(-x[1]))
score=0
visited = {}
for x,y in l:
    day=x
    while day>0:
        if day in visited:
            day-=1
        else:
            break
    if day==0:
        pass
    else:
        visited[day]=True
        score+=y
print(score)
