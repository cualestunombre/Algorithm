global maximum, n
maximum = 0
n=int(input())
l = list(map(int,input().split()))
r = [list(map(int,input().split())) for i in range(n)]
me = int(input())

def backTrack(alive,r,me,nightShift,l):
    global maximum,n
    #밤의 경우
    if len(alive) % 2 == 0:
        #게임 종료 조건
        if len(alive) == 2:
            if nightShift+1 > maximum:
                maximum = nightShift+1
            return
        for i in alive:
            if i != me:
                for _ in range(n):
                    if _ in alive and _ !=i :
                        l[_] += r[i][_]
                backTrack([j for j in alive if j != i],r,me,nightShift+1,l)
                for _ in range(n):
                    if _ in alive and _ !=i :
                        l[_] -= r[i][_]
    #낮의 경우
    else:
        cand = [(i,l[i]) for i in alive ]
        cand.sort(key=lambda x:(-x[1],x[0]))
        seq,_ = cand[0]
        if len(alive) == 2 or seq == me:
            if nightShift > maximum:
                maximum = nightShift
            return
        backTrack([j for j in alive if j != seq],r,me,nightShift,l)
    return




alive = [i for i in range(n)]
backTrack(alive,r,me,0,l)
print(maximum)
