import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
def preOrder(dicArr,bucket,cur,iMap):
    if cur not in dicArr:
        return
    bucket.append(iMap[dicArr[cur][0]])
    preOrder(dicArr,bucket,cur*2,iMap)
    preOrder(dicArr, bucket, (cur * 2)+1,iMap)



def postOrder(dicArr,bucket,cur,iMap):
    if cur not in dicArr:
        return
    postOrder(dicArr, bucket, cur * 2,iMap)
    postOrder(dicArr, bucket, (cur * 2) + 1,iMap)
    bucket.append(iMap[dicArr[cur][0]])

def solution(nodeinfo):
    iMap = {}
    levelMap={}
    for i in range(len(nodeinfo)):
        x,y=nodeinfo[i]
        iMap[x]=i+1
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    dicArr = {}
    newInfo = [[]]
    curVal = nodeinfo[0][1]
    for i in nodeinfo:
        if curVal == i[1]:
            newInfo[-1].append(i)
        else:
            newInfo.append([i])
            curVal=i[1]
    for i in range(len(newInfo)):
        level = i
        start, end = (2 ** level, 2 ** (level + 1) - 1)
        idx = 0
        for x, y in newInfo[i]:
            if i == 0:
                dicArr[1] = (x, y, {"min": -10000000000000000, "max": 10000000000000000})
                levelMap[0]=[1]
            else:
                cand = levelMap[i-1]
                while True:
                    cur = cand[idx]
                    if x<dicArr[cur][0] and x>dicArr[cur][2]["min"]:
                            dicArr[cur*2]=(x,y,{"min":dicArr[cur][2]["min"],"max":dicArr[cur][0]})
                            if i not in levelMap:
                                levelMap[i]=[cur*2]
                            else:
                                levelMap[i].append(cur*2)
                            break
                    if x>dicArr[cur][0] and x<dicArr[cur][2]["max"]:
                            dicArr[cur*2+1]=(x,y,{"min":dicArr[cur][0],"max":dicArr[cur][2]["max"]})
                            if i not in levelMap:
                                levelMap[i]=[cur*2+1]
                            else:
                                levelMap[i].append(cur*2+1)
                            break
                    idx+=1
                    if idx>=len(cand):
                        break
    answer=[[],[]]
    preOrder(dicArr, answer[0], 1,iMap)
    postOrder(dicArr, answer[1], 1,iMap)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))