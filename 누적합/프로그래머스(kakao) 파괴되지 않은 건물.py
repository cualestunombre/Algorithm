global n,m

def valid(x,y):
    global n,m
    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False
def solution(board, skill):
    global n,m
    answer = 0
    n , m = len(board) , len(board[0])
    clone = [[0 for i in range(m)] for j in range(n)]
    typeOp = [0,-1,1]
    for type, r1, c1, r2, c2, degree in skill:
        clone[r1][c1] += degree*typeOp[type]
        if valid(r2+1,c1):
            clone[r2+1][c1] += -degree*typeOp[type]
        if valid(r2+1,c2+1):
            clone[r2+1][c2+1] += degree*typeOp[type]
        if valid(r1,c2+1):
            clone[r1][c2+1] += -degree * typeOp[type]

    for i in range(n):
        cur = 0
        for j in range(m):
            clone[i][j] += cur
            cur = clone[i][j]

    for i in range(m):
        cur = 0
        for j in range(n):
            clone[j][i] += cur
            cur = clone[j][i]
    for  i in range(n):
        for j in range(m):
            board[i][j] += clone[i][j]
            if board[i][j]>0:
                answer += 1
    return answer

