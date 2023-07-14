global minValue
minValue = 100000000000000000
l = [list(map(int,input().split())) for i in range(10)]

def findCur(l):
    for i in range(10):
        for j in range(10):
            if l[i][j] == 1:
                return (i,j)
    return "over"

def cal(cur):
    answer = 0
    for i in cur:
        answer += (5-i)
    return answer

def possible(target,l,ran):
    x,y = target
    if x+ran-1 < 10 and y+ran-1 < 10:
        for i in range(ran):
            for j in range(ran):
                if l[i+x][j+y] != 1:
                    return False
        return True
    return False

def doTheWork(target,l,ran):
    x,y = target
    for i in range(ran):
        for j in range(ran):
            l[i+x][j+y] = 0

def rollBack(target,l,ran):
    x,y = target
    for i in range(ran):
        for j in range(ran):
            l[i+x][j+y] = 1



def bruteForce(l,cur):
    global minValue

    target = findCur(l)

    if target == "over":  # 더 이상 채울 게 없다!!
        answer = cal(cur)
        if answer < minValue:
            minValue = answer
        return

    for index in range(5):
        if cur[index] > 0 and possible(target,l,index+1):

            doTheWork(target,l,index+1)
            cur[index] -= 1

            bruteForce(l,cur)

            cur[index] += 1
            rollBack(target,l,index+1)


    return








bruteForce(l,[5,5,5,5,5])
if minValue == 100000000000000000:
    print(-1)
else:
    print(minValue)