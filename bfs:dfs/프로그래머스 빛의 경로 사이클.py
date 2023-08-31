import sys
sys.setrecursionlimit(500000)
# 로봇의 이동 방향을 상수로 정의 (0:북, 1:동, 2:남, 3:서)
DIR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
answer = []  # 가능한 모든 경로의 이동 횟수를 저장할 리스트

def calMove(x, y, n, m):
    # 그리드를 넘어갈 때 새로운 위치를 계산하는 함수
    return (x % n, y % m)

def calDir(cur, d):
    # 현재 방향과 회전 방향을 고려하여 새로운 방향을 계산하는 함수
    if cur == 'S':
        return d
    elif cur == 'R':
        return (d + 1) % 4
    else:
        return (d - 1) % 4

def search(tx, ty, td, x, y, d, visited, grid,count):
    n, m = len(grid), len(grid[0])
    visited[(x, y, d)] = True
    count+=1
    dx, dy = DIR[d]
    x, y = calMove(x + dx, y + dy, n, m)
    d = calDir(grid[x][y], d)
    if (x, y, d) == (tx, ty, td):
        answer.append(count)
        return
    elif (x, y, d) in visited:
        return
    else:
        search(tx, ty, td, x, y, d, visited, grid,count)
        return


def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = {}
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if(i,j,d) not in visited:
                   search(i, j, d, i, j, d, visited, grid,0)
    answer.sort()
    return answer