from itertools import permutations
from collections import deque

DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]
MAX_DIST = 10 ** 18

def bfs(start, end, l):
    n, m = len(l), len(l[0])
    if cache[start[0]][start[1]][end[0]][end[1]] != -1:
        return cache[start[0]][start[1]][end[0]][end[1]]

    q = deque([(start, 0)])
    visited = {start: 0}

    while q:
        node, dist = q.popleft()
        x, y = node

        for dx, dy in DIR:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < m and l[new_x][new_y] != 'x' and (new_x, new_y) not in visited:
                visited[(new_x, new_y)] = dist + 1
                q.append(((new_x, new_y), dist + 1))
                cache[start[0]][start[1]][new_x][new_y] = cache[new_x][new_y][start[0]][start[1]] = dist + 1
                if (new_x, new_y) == end:
                    return dist + 1

    cache[start[0]][start[1]][end[0]][end[1]] = MAX_DIST
    return MAX_DIST

def cal(cand, l):
    return sum(bfs(cand[i], cand[i + 1], l) for i in range(len(cand) - 1))

def preProcess(l):
    temp = []
    start = (0, 0)
    x, y = len(l), len(l[0])

    for i in range(x):
        for j in range(y):
            if l[i][j] == '*':
                temp.append((i, j))
            if l[i][j] == 'o':
                start = (i, j)
    return temp, start

answer = []
while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    cache = [[[[ -1 for _ in range(max(x, y))] for _ in range(max(x, y))] for _ in range(max(x, y))] for _ in range(max(x, y))]
    l = [input() for _ in range(y)]
    stains, cur = preProcess(l)
    cand = list(permutations(stains))
    answer.append(min([cal([cur] + list(i), l) for i in cand]))

for i in answer:
    print(i if i < MAX_DIST else -1)
