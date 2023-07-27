import sys
sys.setrecursionlimit(100000)

def dp(node, flag, adj, propagator, cache):
    if (node, flag) in cache:
        return cache[(node, flag)]  # 이미 캐시에 값이 있으면 반환

    if len(adj[node]) == 1 and adj[node][0] == propagator:
        # 더 이상 탐색할 노드가 없음
        return 1 if flag == "on" else 0

    value = 0
    if flag == "on":  # 등대가 켜진다면
        for target in adj[node]:
            if target != propagator:
                value += min(dp(target, "on", adj, node, cache),
                             dp(target, "off", adj, node, cache))
    else:  # 등대가 꺼진다면
        for target in adj[node]:
            if target != propagator:
                value += dp(target, "on", adj, node, cache)

    cache[(node, flag)] = value + 1 if flag == "on" else value  # 캐시 저장
    return cache[(node, flag)]

def solution(n, lighthouse):
    adj = {}
    for x, y in lighthouse:
        # 인접 리스트 생성
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)

    cache = {}  # 캐시용 딕셔너리
    return min(dp(1, "on", adj, 0, cache), dp(1, "off", adj, 0, cache))