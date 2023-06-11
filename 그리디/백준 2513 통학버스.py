def findStart(q):
    for i in range(len(q)):
        if q[i][1]!=0:
            return i
    return "nope"


if __name__ =="__main__":
    N,K,S = map(int,input().split()) # 단지, 정원, 학교 위치
    l = [tuple(map(int,input().split())) for i in range(N)]
    l.sort()

    leftQ = []
    rightQ = []

    for pos,count in l:
        if pos<S:
            leftQ.append([pos,count])
        else:
            rightQ.append([pos,count])
    rightQ.reverse()
    dist = 0
    while True:

        leftSeat = K
        startPoint = findStart(leftQ)
        if startPoint == "nope":
            break
        dist += abs(leftQ[startPoint][0] - S) * 2
        for index in range(startPoint,len(leftQ)):
            if leftSeat != 0:
                temp = leftQ[index][1]
                leftQ[index][1] = max(0,leftQ[index][1]-leftSeat)
                leftSeat -= (temp-leftQ[index][1])

            else:
                break
    while True:

        leftSeat = K
        startPoint = findStart(rightQ)
        if startPoint == "nope":
            break
        dist += abs(rightQ[startPoint][0] - S) * 2
        for index in range(startPoint,len(rightQ)):
            if leftSeat != 0:
                temp = rightQ[index][1]
                rightQ[index][1] = max(0,rightQ[index][1]-leftSeat)
                leftSeat -= (temp-rightQ[index][1])

            else:
                break
    print(dist)


