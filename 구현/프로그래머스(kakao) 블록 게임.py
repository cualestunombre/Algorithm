types = [[(0, 1), (0, 2), (1, 2)], [(0, 1), (1, 0), (2, 0)], [(1, 0), (1, 1), (1, 2)],
         [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 0)], [(1, 0), (2, 0), (2, 1)],
         [(1, 0), (1, -1), (1, -2)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (1, -1), (1, 1)],
         [(1, 0), (1, 1), (2, 0)], [(0, 1), (0, 2), (1, 1)], [(1, 0), (1, -1), (2, 0)]
]
blank = [
    [(1,0),(1,1)],[(1,1),(2,1)],[(0,1),(0,2)],[(0,-1),(1,-1)],[(1,1),(1,2)],[(0,1),(1,1)],
    [(0,-1),(0,-2)],[(1,0),(2,0)],[(0,-1),(0,1)],[(0,1),(2,1)],[(1,0),(1,2)],[(0,-1),(2,-1)]
]


def typeCheck(x,y,tp,visited,board,blocks,index):
    n = len(board)
    number = board[x][y]
    for dx,dy in tp:
        if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<n and board[x+dx][y+dy] == number:
            pass
        else:
            return False

    for dx,dy in tp:
        visited[(x+dx,y+dy)] = True

    blocks.append((index,x,y))
    return True

def testHelper(x,y,board):
    for i in range(x+1):
        if board[i][y] != 0:
            return False
    return True


def test(tp,x,y,board):
    d1x,d1y = blank[tp][0]
    d2x,d2y = blank[tp][1]

    t1x ,t1y = x+d1x,y+d1y
    t2x ,t2y = x+d2x,y+d2y

    if testHelper(t1x,t1y,board) and testHelper(t2x,t2y,board):
        return True
    return False
def remove(tp,x,y,board):
    board[x][y] = 0
    for dx,dy in types[tp]:
        board[x+dx][y+dy] = 0

def solution(board):
    blocks, visited = [], {}

    #전처리
    for i in range(len(board)):
        for j in range(len(board)):
            if (i,j) not in visited and board[i][j]!=0:
                for index,tp in enumerate(types):
                    ret = typeCheck(i,j,tp,visited,board,blocks,index)
                    if ret:
                        break
    score = 0
    #게임시작
    while True:
        newOne = []
        toRemove = []
        for tp, x,y in blocks:
            ret = test(tp,x,y,board)
            if ret:
                toRemove.append((tp,x,y))
            else:
                newOne.append((tp,x,y))
        for tp, x,y in toRemove:
            remove(tp,x,y,board)
        if len(newOne) == len(blocks):
            break
        score += len(blocks) - len(newOne)
        blocks = newOne

    return score

solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]])