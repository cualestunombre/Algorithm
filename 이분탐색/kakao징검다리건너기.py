#문제 해설: 이분탐색을 십분발휘해야하는 문제, 중간에 간격을 처리하는 부분을 주의 깊게 볼 것 + 이분탐색에서 <= 이냐 < 이냐의 논의
#이분탐색에서 어차피 경계가 중요하니, 경계부분에 대한 생각을 할 것
import copy
def solution(stones, k):
    arr=[]
    l=copy.deepcopy(stones)
    l.sort()
    start=0
    end=len(l)-1
    while start<=end:
        mid=(start+end)//2
        val=l[mid]
        count=0
        for stone in stones: #간격을 쉽게 처리하는 부분
            if count<k:
                if stone<=val:
                    count+=1
                else:
                    count=0
            else:
                break
        if count>=k:
            arr.append(val)
            end=mid-1
        else:
            start=mid+1
    arr.sort()
    return arr[0]