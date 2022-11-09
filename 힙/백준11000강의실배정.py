import heapq
n=int(input())
l=[tuple(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x:(-x[0]))
count=1
q=[(l[-1][1],l[-1][0])]
l.pop()
while l:
    if q[0][0]>l[-1][0]:
        heapq.heappush(q,(l[-1][1],l[-1][0]))
        l.pop()
        if len(q)>count:
            count = len(q)
    else:
        heapq.heappop(q)
        heapq.heappush(q,(l[-1][1],l[-1][0]))
        l.pop()
print(count)
