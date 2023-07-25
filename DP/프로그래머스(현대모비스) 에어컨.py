import sys
sys.setrecursionlimit(1000000)
global m,n,x1,x2,temp
cache = {}

def backTrack(mode,stage,cur,board):
    #x1이 작은 것 x2가 큰 것
    global m, n, x1, x2, temp

    if (mode,stage,cur) in cache:
        return cache[(mode,stage,cur)]

    if board[stage] == 1 and (cur>x2 or cur<x1): #온도 범위 밖이면 취소
        return 1000000000000000

    if stage == len(board)-1:
        return 0

    if mode == "off": #작동 중지 시
        value = cur
        if temp > cur:
            value += 1
        elif temp < cur:
            value -= 1
        l = [backTrack(a,stage+1,value,board) for a in ["on","off","maintain"]]

        cache[(mode,stage,cur)] = min(l)
        return cache[(mode,stage,cur)]

    if mode == "maintain":
        if cur >=x1 and cur <= x2: #온도 범위일 때
            l = [backTrack(a, stage + 1, cur, board) for a in ["on", "off", "maintain"]]
            cache[(mode,stage,cur)] = min(l) + n

            return cache[(mode,stage,cur)]
        else:
            return 1000000000000000

    if mode == "on":
        l = []
        if temp >= x2:
            l = [backTrack(a,stage + 1,cur -1,board) for a in ["on","off","maintain"]]
        else:
            l = [backTrack(a,stage + 1,cur + 1,board) for a in ["on","off","maintain"]]

        cache[(mode,stage,cur)] = min(l) + m
        return cache[(mode,stage,cur)]

def solution(temperature, t1, t2, a, b, onboard):
    global m,n,x1,x2,temp,minvalue
    m,n,x1,x2,temp  = a,b,t1,t2,temperature
    l = [backTrack(a,0,temperature,onboard) for a in ["on","off","maintain"]]

    return min(l)

solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1])
