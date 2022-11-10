def solution(distance, rocks, n):
    rocks.sort()
    start,end = 0, distance
    while start<=end:
        standard=0
        mid=(start+end)//2
        toDel = 0
        for rock in rocks:
            if rock-standard<mid:
                toDel+=1
            else:
                standard=rock
            if toDel>n:
                break
        if toDel>n:
            end=mid-1
        else:
            start=mid+1
    return end