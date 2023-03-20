import copy as c

def solution(a):
    dic={}
    tempList=c.deepcopy(a)
    tempList.sort()
    targetValue=tempList[0]
    targetIndex=a.index(targetValue)
    dic[targetValue]=True
    dic[a[0]]=True
    dic[a[-1]]=True
    #targetValue기준 왼쪽 search, 왼쪽 search시, 자기 왼쪽의 모든 수보다 작아야 함
    if targetIndex>=2:
        curMax=a[0]
        for index in range(1,targetIndex):
            if curMax<a[index]:
                pass
            else:
                curMax=a[index]
                dic[a[index]]=True
    #targetValue기준 오른쪽 search, 오른쪽 search시, 자기 오른쪽의 모든 수보다 작아야함
    if len(a)-targetIndex>=3:
        curMax=a[-1]
        for index in range(len(a)-2,targetIndex,-1):
            if curMax<a[index]:
                pass
            else:

                curMax=a[index]
                dic[a[index]]=True
    answer = len(dic)
    return answer
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))