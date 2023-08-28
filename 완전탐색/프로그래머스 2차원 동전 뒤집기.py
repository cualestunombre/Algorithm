import itertools


def comp(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                return False
    return True


def makeChange(cand, beginning):
    m = len(beginning)
    n = len(beginning[0])

    for j in cand:
        if j >= 1 and j <= m:
            for i in range(n):
                beginning[j - 1][i] = 1 - beginning[j - 1][i]
        else:
            for i in range(m):
                beginning[i][j - 1 - m] = 1 - beginning[i][j - 1 - m]


def solution(beginning, target):
    m = len(beginning)
    n = len(beginning[0])

    if comp(beginning, target):
        return 0

    for i in range(1, m + n + 1):
        for cand in itertools.combinations(range(1, m + n + 1), i):
            temp = [row[:] for row in beginning]  # 복사
            makeChange(cand, temp)
            if comp(temp, target):
                return i

    return -1

print(solution([[1,1,1,1],[0,1,1,1]],[[0,1,0,1],[1,1 ,1,1]]))
