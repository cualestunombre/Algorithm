import heapq
from itertools import permutations

def partition(n, k, l):
    def partition_helper(n, k, l, current_partition):
        if k == 1:
            if n >= current_partition[-1]:
                current_partition.append(n)
                l.append(current_partition)
            return
        for i in range(1, n):
            if i >= current_partition[-1]:
                partition_helper(n - i, k - 1, l, current_partition + [i])
    if n < k:
        return
    partition_helper(n, k, l, [0])

def simulate(k, n, regs, l):
    wait = 0

    heaps = [[] for _ in range(k + 1)]
    cands = [[] for _ in range(k + 1)]
    count = [0 for _ in range(k + 1)]
    regs.sort(key=lambda x: (x[2], x[0]))

    for a, b, c in regs:
        if l[c - 1] != len(heaps[c]):
            heapq.heappush(heaps[c], a + b)
        else:
            cands[c].append((a, b))
        count[c] += 1

    for i in range(1, len(heaps)):
        if not heaps[i] and count[i] != 0:
            return 10**18  # 대략적인 무한대 값으로 설정

    for i in cands:
        i.sort(reverse=True)

    for i in range(1, k + 1):
        while heaps[i]:
            endTime = heapq.heappop(heaps[i])
            if not cands[i]:
                break
            elif cands[i][-1][0] < endTime:
                wait += endTime - cands[i][-1][0]
                heapq.heappush(heaps[i], endTime + cands[i][-1][1])
                cands[i].pop()
            else:
                heapq.heappush(heaps[i], cands[i][-1][0] + cands[i][-1][1])
                cands[i].pop()

    return wait

def solution(k, n, reqs):
    minValue = 100000000000000000
    ret = []
    l = set()
    partition(n,k,ret)

    for i in ret:
        temp = list(permutations(i))
        for j in temp:
            l.add(tuple(j))

    for i in l:
        value = simulate(k,n,reqs,i)
        if value < minValue:
            minValue = value

    return minValue










