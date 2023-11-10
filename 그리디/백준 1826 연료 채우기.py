import heapq
n = int(input())
flag = True
stations = sorted([tuple(map(int,input().split())) for i in range(n)])
dist, gas = map(int,input().split())
stations.append((dist,0))
heap = []
cur,count = 0,0

for station in stations:
 gas -= (station[0] - cur)
 if gas < 0 and heap:
  while heap and gas<0:
   gas += -heapq.heappop(heap)
   count += 1

 if gas < 0:
  flag = False
  break
 heapq.heappush(heap,-station[1])
 cur = station[0]

if flag:
 print(count)
else:
 print(-1)


