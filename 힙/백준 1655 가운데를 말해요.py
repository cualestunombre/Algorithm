import heapq
import heapq as pq
n = int(input())
median = -1
answer = []
minHeap, maxHeap = [],[]
for i in range(1,n+1):
    number = int(input())
    if i == 1:
        median = number
        answer.append(median)
    
    elif i % 2 == 0 : #짝수의 경우
        if number < median:
            heapq.heappush(maxHeap,-number)
        else:
            heapq.heappush(minHeap,number)
        cand = -1
        if len(maxHeap) > len(minHeap):
            cand = -maxHeap[0]
        else:
            cand = minHeap[0]
        answer.append(min(median,cand))
    else:
        cand = -1
        if len(maxHeap) > len(minHeap):
            cand = -pq.heappop(maxHeap)
        else:

            cand = pq.heappop(minHeap)
        temp = sorted([cand,number,median])
        pq.heappush(maxHeap,-temp[0]), pq.heappush(minHeap,temp[2])
        median = temp[1]
        answer.append(median)



for i in answer:
    print(i)