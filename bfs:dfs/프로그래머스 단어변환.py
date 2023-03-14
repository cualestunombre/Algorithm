global mini
mini=1000000


def compare(a,b):
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    if count==1:
        return True
    else:
        return False


def dfs(cur,visited,words,target,cnt):
    global mini
    if cur==target:
        if mini>cnt:
            mini=cnt
        return
    for i in words:
        if compare(i,cur):
            if i not in visited:
                visited[i]=True
                dfs(i,visited,words,target,cnt+1)
                del visited[i]
    return


def solution(begin, target, words):
    for i in words:
        visited={}
        visited[begin]=True
        if compare(begin,i):
            visited[i]=True
            dfs(i,visited,words,target,1)
    if mini==1000000:
        return 0
    else:
        return mini
