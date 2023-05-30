import math

cache={0:1,1:1}
def get_partitions(n):
    partitions = []
    partition_helper(n, n, [], partitions)
    return partitions

def partition_helper(n, max_val, current_partition, partitions):
    if n == 0:
        partitions.append(current_partition)
        return
    for i in range(min(max_val, n), 0, -1):
        partition_helper(n - i, i, current_partition + [i], partitions)

def solution(n):
    if n in cache:
        return cache[n]
    l=get_partitions(n)
    __sum=0
    for i in l:
        _sum=1
        temp={}
        for j in i:
            if j not in temp:
                temp[j]=1
            else:
                temp[j]+=1
            _sum*=solution(j-1)
        val = (math.factorial(len(i)))  * _sum
        for x in temp:
            if temp[x]>=2:
                val = val//math.factorial(temp[x])
        __sum += val
    cache[n]=__sum

    return cache[n]
print(solution(14))