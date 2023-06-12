import sys
sys.setrecursionlimit(10000)
cache = []
adj = []
n = int(input())
seq = list(map(str, input().split()))
m, k = map(int, input().split())

def dp(x, y):
    global n, cache
    if cache[x][y] != -1:
        return cache[x][y]
    if y == n:
        return 0
    _max = 0
    for target, color in adj[x]:
        value = dp(target, y + 1)
        if color == seq[y]:
            value += 10
        if value > _max:
            _max = value
    cache[x][y] = _max
    return _max

# Initialize cache and adj
cache = [[-1] * (n + 1) for _ in range(m + 1)]
adj = [[] for _ in range(m + 1)]

for i in range(k):
    f, t, c = map(str, input().split())
    f = int(f)
    t = int(t)
    if not adj[f]:
        adj[f].append((t, c))
    else:
        adj[f].append((t, c))
    if not adj[t]:
        adj[t].append((f, c))
    else:
        adj[t].append((f, c))

print(dp(1, 0))
