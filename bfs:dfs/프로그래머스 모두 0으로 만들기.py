import sys
sys.setrecursionlimit(300000)

class StaticClass:
    count = 0

def checkAll(a):
    # 배열 a의 모든 요소가 0인지 확인하는 함수
    for ele in a:
        if ele != 0:
            return False
    return True

# 전처리 함수
def preProcess(rel, edges):
    for ele in edges:
        x, y = ele[0], ele[1]
        # rel 딕셔너리에 x가 없는 경우, 새로운 키로 추가하고 y를 값으로 설정
        if x not in rel:
            rel[x] = [y]
        else:
            rel[x].append(y)
        # rel 딕셔너리에 y가 없는 경우, 새로운 키로 추가하고 x를 값으로 설정
        if y not in rel:
            rel[y] = [x]
        else:
            rel[y].append(x)

def dfs(caller, target, rel, a):
    adj = rel[target]
    # adj가 [caller]로만 이루어져 있는 경우, caller 노드와 target 노드만 연결된 경우
    if len(adj) == 1 and adj[0] == caller:
        value = a[target]
        a[target] = 0
        a[caller] += value
        StaticClass.count += abs(value)
        return
    for node in adj:
        if node != caller:
            # caller가 아닌 다른 노드에 대해 dfs 재귀 호출
            dfs(target, node, rel, a)
    if caller != -1:
        value = a[target]
        a[target] = 0
        a[caller] += value
        StaticClass.count += abs(value)
    return

def solution(a, edges):
    rel = {}
    preProcess(rel, edges)
    dfs(-1, 0, rel, a)
    flag = checkAll(a)
    return StaticClass.count if flag else -1
