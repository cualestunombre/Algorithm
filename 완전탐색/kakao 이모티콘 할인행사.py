from itertools import product
def solution(users, emoticons):
    answer = []
    for i in product([10,20,30,40],repeat=len(emoticons)): #특정 할인율에 대해
        sales=0
        signUp=0
        for j, k in users:
            total=0
            for v in range(len(emoticons)):
                if i[v]>=j:
                    total+=int((emoticons[v]*(100-i[v]))/100)
            if total>=k:
                signUp+=1
            else:
                sales+=total
        answer.append([signUp,sales])
    answer.sort(key=lambda x:(-x[0],-x[1]))



    return answer[0]