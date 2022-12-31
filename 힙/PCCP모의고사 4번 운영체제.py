import heapq as pq
def solution(program):
    count={}
    answer=[]
    heap = []
    endtime=0
    program.sort(key=lambda x:(-x[1],-x[0]))
    while heap or program:
        if heap: #힙에는 종료시간 전에것 만 넣을 것
            score,time,runtime=pq.heappop(heap)
            if score in count:
                count[score]+=endtime-time
            else:
                count[score]=endtime-time
            endtime = endtime + runtime
        else:
            score,time,runtime=program.pop()
            endtime=time+runtime
        while program and program[-1][1]<=endtime:
            score,time,runtime=program.pop()
            pq.heappush(heap,(score,time,runtime))
    answer.append(endtime)
    for i in range(1,11):
        if i in count:
            answer.append(count[i])
        else:
            answer.append(0)
    return answer





