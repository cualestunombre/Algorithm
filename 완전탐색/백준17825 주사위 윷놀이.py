from itertools import product
class StaticClass:
    max = 0
    dist = []

class Node:
    def __init__(self,score,next1,next2):
        self.score = score
        self.next1 = next1
        self.next2 = next2
def initNode(node):
    node2 = Node(2,None,None)
    node4 = Node(4,None,None)
    node6 = Node(6,None,None)
    node8 = Node(8,None,None)
    node10 = Node(10,None,None)
    node12 = Node(12,None,None)
    node13 = Node(13,None,None)
    node14 = Node(14,None,None)
    node16 = Node(16,None,None)
    node16s = Node(16, None, None)
    node18 = Node(18,None,None)
    node20= Node(20,None,None)
    node19 = Node(19,None,None)
    node22 = Node(22,None,None)
    node22s = Node(22,None,None)
    node24 = Node(24,None,None)
    node24s = Node(24,None,None)
    node25 = Node(25,None,None)
    node26 = Node(26,None,None)
    node26s = Node(26,None,None)
    node27 = Node(27,None,None)
    node28 = Node(28,None,None)
    node28s = Node(28,None,None)
    node30 = Node(30,None,None)
    node30s = Node(30,None,None)
    node32 = Node(32,None,None)
    node34 = Node(34,None,None)
    node35 = Node(35,None,None)
    node36 = Node(36,None,None)
    node38 = Node(38,None,None)
    node40 = Node(40,None,None)
    nodeEnd = Node(0,None,None)

    node.next1 = node2
    node2.next1 = node4
    node4.next1 = node6
    node6.next1 = node8
    node8.next1 = node10
    node10.next1 = node12
    node10.next2 = node13
    node12.next1 = node14
    node14.next1 = node16
    node16.next1 = node18
    node18.next1 = node20
    node20.next1 = node22s
    node20.next2 = node22
    node22s.next1 = node24s
    node24s.next1 = node26s
    node26s.next1 = node28s
    node28s.next1 = node30s
    node30s.next1 = node32
    node30s.next2 = node28
    node32.next1 = node34
    node34.next1 = node36
    node36.next1 = node38
    node38.next1 = node40
    node22.next1 = node24
    node24.next1 = node25
    node25.next1 = node30
    node30.next1 = node35
    node35.next1 = node40
    node28.next1 = node27
    node27.next1 = node26
    node26.next1 = node25
    node13.next1 = node16s
    node16s.next1 = node19
    node19.next1 = node25
    node40.next1 = nodeEnd

def initPieces():
    node = [0, 1, 2, 3]
    permutations = list(product(node, repeat=10))
    return permutations

def move(position,cur,distance,turn):
    if cur.next1==None:
        return (False,0)
    if cur.next2 != None:
        distance-=1
        cur = cur.next2
        while distance>=1:
            distance-=1
            if cur.next1 != None:
                cur = cur.next1
            else:
                break

    else:
        while distance>=1:
            distance-=1
            if cur.next1 != None:
                cur = cur.next1
            else:
                break
    for piece in position:
        if position[piece] is cur and cur.next1!=None:
            return (False,0)

    position[turn] = cur
    return (True,cur.score)

def playGame(sequence,position):
    totalScore = 0
    relic = []
    for index,turn in enumerate(sequence):

        flag,score = move(position,position[turn],StaticClass.dist[index],turn)
        if not flag:
            return
        relic.append((turn,StaticClass.dist[index]))
        totalScore += score
    if StaticClass.max < totalScore:
        StaticClass.max = totalScore






if __name__ =="__main__":
    dist = list(map(int,input().split()))
    StaticClass.dist = dist
    position = {}
    firstNode = Node(0,None,None)
    initNode(firstNode)
    permutations = initPieces()
    for sequence in permutations:
        for ele in [0,1,2,3]:
            position[ele] = firstNode
        playGame(sequence,position)

    print(StaticClass.max)




