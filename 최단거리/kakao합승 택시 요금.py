def solution(n, s, a, b, fares):
    dist=[[1000000000000 for i in range(n+1)] for j in range(n+1)]
    for i,j,f in fares:
        dist[i][j]=f
        dist[j][i]=f
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    dist[i][j]=0
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    min=1000000000000
    for i in range(1,n+1):
        if dist[s][i]+dist[i][a]+dist[i][b]<min:
            min=dist[s][i]+dist[i][a]+dist[i][b]
    return min
n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))