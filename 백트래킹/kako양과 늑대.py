maxx=0
def backtracking(info,edge,cur,score,visited,eaten):
    global maxx
    sheep,wolf=score
    if sheep>maxx:
        maxx=sheep
    if sheep<=wolf:
        return
    for i in edge[cur]:
        if i not in visited:
            if i in eaten:
                visited[i]=True
                backtracking(info,edge,i,score,visited,eaten)
                del visited[i]
            else:
                if info[i]==1:
                    eaten[i]=True
                    backtracking(info,edge,i,(sheep,wolf+1),{i:True},eaten)
                    del eaten[i]
                else:
                    eaten[i]=True
                    backtracking(info, edge, i, (sheep+1, wolf), {i:True}, eaten)
                    del eaten[i]


def solution(info, edges):
    global maxx
    edge={}
    visited={0:True}
    eaten={0:True}
    for i in edges:
        x,y=i
        if x in edge:
            edge[x]+=[y]
        else:
            edge[x]=[y]
        if y in edge:
            edge[y]+=[x]
        else:
            edge[y]=[x]
    backtracking(info,edge,0,(1,0),visited,eaten)
    return maxx
