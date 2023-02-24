import heapq as pq
n=int(input())
l=[tuple(map(int,input().split())) for i in range(n)]
l.sort()
q=[]
for deadline,ramen in l:
    pq.heappush(q,ramen)
    if deadline<len(q):
        pq.heappop(q)
print(sum(q))
