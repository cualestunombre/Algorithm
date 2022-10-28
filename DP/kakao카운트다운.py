import sys
limit_number = 300000
sys.setrecursionlimit(limit_number)
sequence=[1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5,50,20]
cache={}
def solution(target):

    def dp(n):
        if n==0:
            return (0,0) #횟수, 합
        if n in cache:
            return cache[n]
        arr=[]
        #싱글,불
        for i in sequence:
            if i==50:
                if n-50>=0:
                    temp = dp(n-50)
                    arr.append((temp[0]+1,temp[1]+1))
            else:
                if n-i>=0:
                    temp = dp(n-i)
                    arr.append((temp[0]+1,temp[1]+1))
                if n-i*2>=0:
                    temp = dp(n-i*2)
                    arr.append((temp[0]+1,temp[1]))
                if n-i*3>=0:
                    temp = dp(n-i*3)
                    arr.append((temp[0]+1,temp[1]))
        arr.sort(key=lambda x:(x[0],-x[1]))
        cache[n]=arr[0]
        return cache[n]
    ans = dp(target)
    answer = [ans[0],ans[1]]
    return answer
print(solution(2022))
print(cache[60])