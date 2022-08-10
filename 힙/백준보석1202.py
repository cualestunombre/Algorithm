import heapq as pq
values=0
n , k = map(int, input().split())
gem = [tuple(map(int,input().split())) for i in range(n)]
bags = [int(input()) for i in range(k)]
bags.sort(reverse=True)
gem.sort(key=lambda x:(-x[0],-x[1]))
q=[]
answer=[]
while bags:
    while True:
        if not gem:
            break
        if gem[len(gem)-1][0]<=bags[len(bags)-1]:
            x,y=gem.pop()
            pq.heappush(q,(-y,x))
        else:
            break
    bag=bags.pop()
    if q:
        sample=pq.heappop(q)
        if bag>=sample[1]:
            values+= (-sample[0])
        else:
            pq.heappush(q,sample)
print(values)
# 두가지 기준을 컨트롤하기에 최적화된 힙기법
