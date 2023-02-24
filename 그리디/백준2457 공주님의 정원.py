import heapq as pq
from collections import deque
n = int(input())
l=[]
for i in range(n):
    a,b,c,d = map(str,input().split())
    if len(b)==1:
        b="0"+b
    if len(d)==1:
        d="0"+d
    l.append((int(a+b),int(c+d)))
l.sort()
lq = deque(l)
sTarget=301
eTarget=1201
count=0
done=False
while True:
    q=[]
    while True and lq:
        if lq[0][0]<=sTarget:
            x,y=lq.popleft()
            pq.heappush(q,(-y,x))
        else:
            break
    if not q:
        break
    y,x=pq.heappop(q)
    if -y>=eTarget:
        done=True
        count+=1
        break
    else:
        count+=1
        sTarget=-y
if done:
    print(count)
else:
    print(0)











