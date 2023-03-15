global matrix
cache={}
def dp(ran):
    x,y=ran
    if (x,y) in cache:
        return cache[(x,y)]
    if x==y:
        return 0
    minimum=10000000000000000000
    for i in range(x,y):
        if dp((x,i))+dp((i+1,y))+matrix[x][0]*matrix[i+1][0]*matrix[y][1]<minimum:
            minimum=dp((x,i))+dp((i+1,y))+matrix[x][0]*matrix[i+1][0]*matrix[y][1]
            cache[ran]=minimum
    return  cache[ran]


def solution(matrix_sizes):
    global matrix
    matrix=matrix_sizes
    answer = dp((0,len(matrix)-1))
    return answer

