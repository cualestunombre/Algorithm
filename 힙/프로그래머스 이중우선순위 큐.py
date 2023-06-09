import heapq

def solution(operations):
    deleted = {}
    min_heap = []
    max_heap = []
    for index, operation in enumerate(operations):
        command, number = operation.split()
        number = int(number)
        if command == "I":
            heapq.heappush(min_heap,(number,index))
            heapq.heappush(max_heap,(-number,index))
        elif command=="D" and number==1:
            while max_heap:
                node = heapq.heappop(max_heap)
                if node in deleted:
                    continue
                else:
                    deleted[(-node[0],node[1])]=True
                    break
        else:
            while min_heap:
                node = heapq.heappop(min_heap)
                if node in deleted:
                    continue
                else:
                    deleted[node]=True
                    break
    ret = [ele[0] for ele in min_heap if ele not in deleted]
    ret.sort()
    return [ret[-1],ret[0]] if ret else [0,0]

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])