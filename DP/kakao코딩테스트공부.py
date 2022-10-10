def solution(alp, cop, problems):
    maxa=0 #최종 타겟 알고력
    maxc=0 #최종 타겟 코딩력
    for a,b,c,d,e in problems:
        if a>maxa:
            maxa=a
        if b>maxc:
            maxc=b
    dp={}
    dp[(alp,cop)]=0
    if alp>maxa:
        maxa=alp
    if cop>maxc:
        maxc=cop
    for i in range(alp,maxa+1):
        for j in range(cop,maxc+1):
            if (i,j+1) not in dp:
                dp[(i,j+1)]=dp[(i,j)]+1
            else:
                dp[(i,j+1)]=min(dp[(i,j)]+1,dp[(i,j+1)])
            if (i+1,j) not in dp:
                dp[(i+1,j)]=dp[(i,j)]+1
            else:
                dp[(i+1,j)]=min (dp[(i,j)]+1,dp[(i+1,j)])
            for a,b,c,d,e in problems: #필요 알고력,필요 코딩력,증가 알고력, 증가 코딩력, 시간
                if i>=a and j>=b:
                    targetA = min(maxa,i+c)
                    targetC = min(maxc,j+d)
                    if (targetA,targetC) not in dp:
                        dp[(targetA,targetC)]=dp[(i,j)]+e
                    else:
                        dp[(targetA,targetC)]=min(dp[(targetA,targetC)],dp[(i,j)]+e)

    return dp[(maxa,maxc)]
print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))