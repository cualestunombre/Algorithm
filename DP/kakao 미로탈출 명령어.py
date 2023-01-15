import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
cache={}
dir=[(1,0),(0,-1),(0,1),(-1,0)]
seq=['d','l','r','u']
def solution(n, m, x, y, r, c, k):
    def dp(na,nb,nc,nd,ne):
        if ne<0:
            return '#'
        if ne==0 and na==nc and nb==nd:
            return ''
        if (na,nb,nc,nd,ne) in cache:
            return cache[(na,nb,nc,nd,ne)]
        count=-1
        word='#'
        for dx,dy in dir:
            count+=1
            if na+dx<=n and na+dx>=1 and nb+dy<=m and nb+dy>=1:
                val = dp(na+dx,nb+dy,nc,nd,ne-1)
                if val!='#':
                    word = seq[count]+val
                    break
        cache[na,nb,nc,nd,ne]=word
        return word

    answer = dp(x,y,r,c,k)
    if answer=='#':
        return 'impossible'
    else:
        return answer
print(solution(3,4,2,3,3,1,5))
